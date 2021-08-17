#Copyright Deng（灯哥） (ream_d@yeah.net)  Py-apple dog project
#Github:https://github.com/ToanTech/py-apple-quadruped-robot
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at:http://www.apache.org/licenses/LICENSE-2.0
from math import sin,cos,pi,atan,tan
from machine import I2C, Pin
import padog
import PA_IMU
import PA_AVGFILT
import array

#中间变量设定
x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
cg_adjust=0
xs=0
faai=0.5
Ts=1
q=[]
#设置陀螺仪 IIC 接口
try:
  i2cc = I2C(scl=Pin(22), sda=Pin(21))   #集成板
  acc = PA_IMU.accel(i2cc)
  acc.error_gy()
except:
  i2cc = I2C(scl=Pin(32), sda=Pin(33))   #直插板
  acc = PA_IMU.accel(i2cc)
  acc.error_gy()

#滑动平均滤波(PITCH 轴)
gyro_data_p = array.array('i', [0]*10)
f_gyro_data_p = PA_AVGFILT.avg_filiter(gyro_data_p)

def cal_adjust(CG_Y,l,xk,sita,period):   #计算重心偏移量函数,使得机器人重心投影始终落在三角形面
  result=(CG_Y+period*(l+xk)/4+110*tan(sita*1.5))  #计算高度暂时固定在典型的110,1.5是角度P环值
  #print(result)   #打印出调整量，用于调试
  return result
  

def cal_w(CG_X,CG_Y,l,xf,h,speed,t,r1,r4,r2,r3):   #WALK步态主计算函数，相序 1-2-3-4
    global d,z
    global x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s
    global q,sita,cg_adjust
    
    #获得陀螺仪数据
    ay=acc.get_values()
    q=PA_IMU.IMUupdate(ay["GyX"]/65.5*0.0174533,ay["GyY"]/65.5*0.0174533,ay["GyZ"]/65.5*0.0174533,ay["AcX"]/8192,ay["AcY"]/8192,ay["AcZ"]/8192)
    try:
      gyro_p=f_gyro_data_p.avg(round(q[1]))
    except:
      pass
      
    #开始步态计算
    if t<Ts*faai:    #迈出腿1
        #print("腿1")
        padog.gesture(0,CG_X,cal_adjust(CG_Y,0,l,gyro_p*pi/180,-1))   #粗调重心
        if abs(padog.X_S-padog.X_goal)<3:
          padog.gesture(0,CG_X,cal_adjust(CG_Y,0,l,gyro_p*pi/180,-1))  #微调重心
          padog.t=padog.t+speed
          sigma=2*pi*t/(faai*Ts)
          zep=h*(1-cos(sigma))/2
          xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
          #输出y
          y1=zep
          y2=0
          y3=0
          y4=0
          #输出x
          x1=xep_b*r1
          x2=0
          x3=0
          x4=0
          x1_s=x1;x2_s=x2;x3_s=x3;x4_s=x4;y1_s=y1;y2_s=y2;y3_s=y3;y4_s=y4
        return x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s

    if t>=Ts*faai and t<2*Ts*faai:    #迈出腿2
        #print("腿2")
        padog.gesture(0,CG_X,cal_adjust(CG_Y,l,0,gyro_p*pi/180,-1))
        if abs(padog.X_S-padog.X_goal)<3:
          padog.gesture(0,CG_X,cal_adjust(CG_Y,l,0,gyro_p*pi/180,-1))
          padog.t=padog.t+speed
          t=t-faai*Ts
          sigma=2*pi*t/(faai*Ts)
          zep=h*(1-cos(sigma))/2
          xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
          #输出y
          y1=0
          y2=zep
          y3=0
          y4=0
          #输出x
          x1=xf
          x2=xep_b*r2
          x3=0
          x4=0
          x1_s=x1;x2_s=x2;x3_s=x3;x4_s=x4;y1_s=y1;y2_s=y2;y3_s=y3;y4_s=y4
        return x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s
    if t>=2*Ts*faai and t<3*Ts*faai:    #迈出腿3
        #print("腿3")
        padog.gesture(0,CG_X,cal_adjust(CG_Y,l,xf,gyro_p*pi/180,1))
        if abs(padog.X_S-padog.X_goal)<3:
          padog.gesture(0,CG_X,cal_adjust(CG_Y,l,xf,gyro_p*pi/180,1))
          padog.t=padog.t+speed
          t=t-faai*Ts*2
          sigma=2*pi*t/(faai*Ts)
          zep=h*(1-cos(sigma))/2
          xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
          #输出y
          y1=0
          y2=0
          y3=zep
          y4=0
          #输出x
          x1=xf
          x2=xf
          x3=xep_b*r3
          x4=0
          x1_s=x1;x2_s=x2;x3_s=x3;x4_s=x4;y1_s=y1;y2_s=y2;y3_s=y3;y4_s=y4
        return x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s

    if t>=3*Ts*faai and t<4*Ts*faai:    #迈出腿4
        #print("腿4")
        padog.gesture(0,CG_X,cal_adjust(CG_Y,l,xf,gyro_p*pi/180,1))
        if abs(padog.X_S-padog.X_goal)<3:
          padog.gesture(0,CG_X,cal_adjust(CG_Y,l,xf,gyro_p*pi/180,1))
          padog.t=padog.t+speed
          t=t-faai*Ts*3
          sigma=2*pi*t/(faai*Ts)
          zep=h*(1-cos(sigma))/2
          xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
          #输出y
          y1=0
          y2=0
          y3=0
          y4=zep
          #输出x
          x1=xf
          x2=xf
          x3=xf
          x4=xep_b*r4
          x1_s=x1;x2_s=x2;x3_s=x3;x4_s=x4;y1_s=y1;y2_s=y2;y3_s=y3;y4_s=y4
        return x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s
    if t>=4*Ts*faai:    #足端坐标归零
        padog.gesture(0,CG_X,CG_Y)
        if x1_s>0:
          x1_s=x1_s-x1_s*0.1
        elif x1_s<0:
          x1_s=x1_s+x1_s*0.1
        x2_s=x1_s;x3_s=x1_s;x4_s=x1_s
        if abs(padog.X_S-padog.X_goal)<1 and abs(x1_s)<1:
          padog.t=padog.t+0.1
        return x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s




