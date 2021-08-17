import math
import machine
from time import sleep,sleep_ms
Kp=0.8 #比例增益支配率收敛到加速度计/磁强计
Ki=0.001 #积分增益支配率的陀螺仪偏见的衔接
halfT=0.004 #采样周期的一半
q0=1
q1=0
q2=0
q3=0; #四元数的元素 ,代表估计方向
exInt=0
eyInt=0
ezInt=0 #按比例缩小积分误差

def IMUupdate(gx,gy,gz,ax,ay,az):
    K=0.7
    a=[0,0,0,0,0,0,0,0]
    global Kp,Ki,halfT,q0,q1,q2,q3,exInt,eyInt,ezInt
    if ax!=0 or ay!=0 or az!=0: 
        norm=math.sqrt(ax*ax+ay*ay+az*az);
    ax=ax/norm; #单位化
    ay=ay/norm;
    az=az/norm;
    #估计方向的重力
    vx=2* (q1*q3-q0*q2 );
    vy=2* (q0*q1+q2*q3 );
    vz=q0*q0-q1*q1-q2*q2+q3*q3;
    #错误的领域和方向传感器测量参考方向之间的交叉乘积的总和
    ex= (ay*vz-az*vy );
    ey= (az*vx-ax*vz );
    ez= (ax*vy-ay*vx );
    #积分误差比例积分增益
    exInt=exInt+ex*Ki;
    eyInt=eyInt+ey*Ki;
    ezInt=ezInt+ez*Ki;
    #调整后的陀螺仪测量
    gx=gx+Kp*ex+exInt;
    gy=gy+Kp*ey+eyInt;
    gz=gz+Kp*ez+ezInt;
    #整合四元数率和正常化
    q0=q0+ (-q1*gx-q2*gy-q3*gz )*halfT;
    q1=q1+ (q0*gx+q2*gz-q3*gy )*halfT;
    q2=q2+ (q0*gy-q1*gz+q3*gx )*halfT;
    q3=q3+ (q0*gz+q1*gy-q2*gx )*halfT;
    #正常化四元
    norm=math.sqrt(q0*q0+q1*q1+q2*q2+q3*q3 );
    q0=q0/norm;
    q1=q1/norm;
    q2=q2/norm;
    q3=q3/norm;
    Pitch=math.asin (-2*q1*q3+2*q0*q2 )*57.3; #pitch ,转换为度数
    if -2*q1*q1-2*q2*q2+1!=0:
        Roll=math.atan ((2*q2*q3+2*q0*q1)/(-2*q1*q1-2*q2*q2+1) )*57.3; #rollv
    a[0]=Pitch
    a[1]=Roll
    if ay*ay+az*az!=0:
        a[2]=-math.atan(ax/math.sqrt(ay*ay+az*az))*57.2957795
    if ax*ax+az*az!=0:
        a[3]=math.atan(ay/math.sqrt(ax*ax+az*az))*57.2957795
    a[4]=gx
    a[5]=gy
    a[6]=gz
    a[0]=-K*Pitch-(1-K)*a[2]
    a[1]=K*Roll+(1-K)*a[3]
    return a

class accel():
    error=[0,0,0]
    def __init__(self, i2c, addr=0x68):
        self.iic = i2c
        self.addr = addr
        self.iic.start()
        sleep_ms(1)
        self.iic.writeto(self.addr, bytearray([107, 0]))
        sleep_ms(1)
        self.iic.writeto_mem(self.addr,0x19,b'\x07') #gyro 125hz
        sleep_ms(1)
        self.iic.writeto_mem(self.addr,0x1a,b'\x04')  #low filter 21hz
        sleep_ms(1)
        self.iic.writeto_mem(self.addr,0x1b,b'\x08') #gryo 500/s 65.5lsb/g
        sleep_ms(1)
        self.iic.writeto_mem(self.addr,0x1c,b'\x08') #acceler 4g ,8192lsb.g
        sleep_ms(1)
        self.iic.stop()

    def get_raw_values(self):
        self.iic.start()
        a = self.iic.readfrom_mem(self.addr, 0x3B, 14)
        self.iic.stop()
        return a

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def error_gy(self):
        sleep(3)
        global error
        error=[0,0,0]
        vals = {}
        for i in range(0,10):
	            raw_ints = self.get_raw_values()
	            vals["GyX"] = self.bytes_toint(raw_ints[8], raw_ints[9])
	            vals["GyY"] = self.bytes_toint(raw_ints[10], raw_ints[11])
	            vals["GyZ"] = self.bytes_toint(raw_ints[12], raw_ints[13])
	            error[0]= error[0]+vals["GyX"]
	            error[1]= error[1]+vals["GyY"]
	            error[2]= error[2]+vals["GyZ"]
	            sleep_ms(8)
        error[1]=error[1]/10.0
        error[2]=error[2]/10.0
        error[0]=error[0]/10.0
		
    def get_values(self):
        global error
        vals = {}
        raw_ints = self.get_raw_values()
        vals["AcX"] = self.bytes_toint(raw_ints[0], raw_ints[1])
        vals["AcY"] = self.bytes_toint(raw_ints[2], raw_ints[3])
        vals["AcZ"] = self.bytes_toint(raw_ints[4], raw_ints[5])
        vals["Tmp"] = self.bytes_toint(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        vals["GyX"] = self.bytes_toint(raw_ints[8], raw_ints[9])-error[0]
        vals["GyY"] = self.bytes_toint(raw_ints[10], raw_ints[11])-error[1]
        vals["GyZ"] = self.bytes_toint(raw_ints[12], raw_ints[13])-error[2]
        #vals["GyZ1"] = self.bytes_toint(raw_ints[12], raw_ints[13])
        return vals  # returned in range of Int16
        # -32768 to 32767



