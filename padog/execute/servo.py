from __future__ import division                             #导入 __future__ 文件的 division 功能函数(模块、变量名....)   #新的板库函数  //=
import time
 
# Import the PCA9685 module.
import Adafruit_PCA9685                                     #导入Adafruit_PCA9685模块
 
 
# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)                   #调试打印日志输出
 
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()                            #把Adafruit_PCA9685.PCA9685()引用地址赋给PWM标签
                         #180du
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
 
 
#2^12精度  角度转换成数值  #angle输入的角度值(0--180)  #pulsewidth高电平占空时间(0.5ms--2.5ms)   #/1000将us转换为ms  #20ms时基脉冲(50HZ)
#pulse_width=((angle*11)+500)/1000;  //将角度转化为500(0.5)<-->2480(2.5)的脉宽值(高电平时间)   angle=180时  pulse_width=2480us(2.5ms)
#date/4096=pulse_width/20 ->有上pulse_width的计算结果得date=4096*( ((angle*11)+500)/1000 )/20   -->int date=4096((angle*11)+500)/20000;
         
def set_servo_angle(channel, angle):                    #输入角度转换成12^精度的数值
    date=4096*((angle*11)+500)/20000                #进行四舍五入运算 date=int(4096*((angle*11)+500)/(20000)+0.5)   
    date=int(date)
    pwm.set_pwm(channel, 0, date)
 
 
# Set frequency to 50hz, good for servos.
pwm.set_pwm_freq(50)

""" 
print('Moving servo on channel x, press Ctrl-C to quit...')
while True:
        # Move servo on channel O between extremes.
    channel=int(input('pleas input channel:'))
    angle=int(input('pleas input angle:'))
    set_servo_angle(channel, angle)
    #time.sleep(1)
"""
class servos:
    def position(index, degrees=None):
        set_servo_angle(index, degrees)
