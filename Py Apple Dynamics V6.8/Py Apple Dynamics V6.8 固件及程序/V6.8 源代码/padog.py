#Copyright Deng（灯哥） (ream_d@yeah.net)  Py-apple dog project
#Github:https://github.com/ToanTech/py-apple-quadruped-robot
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at:http://www.apache.org/licenses/LICENSE-2.0

#引入模块
import PA_SERVO
import PA_TROT
import PA_WALK
import PA_IK
import PA_ATTITUDE
import PA_STABLIZE
import time
from machine import Pin

led=Pin(22,Pin.OUT)
led.value(0)        #Open LED
#连接网络，启用WEBREPL
selfadd=0

def do_connect_STA(essid, password):
    global selfadd
    import network 
    wifi = network.WLAN(network.STA_IF)  
    if not wifi.isconnected(): 
        print('connecting to network...')
        wifi.active(True) 
        wifi.connect(essid, password) 
        while not wifi.isconnected():
            pass 
    print('network config:', wifi.ifconfig())
    selfadd=wifi.ifconfig()[0]

def do_connect_AP():
    global selfadd
    import network 
    wifi = network.WLAN(network.AP_IF)  
    if not wifi.isconnected(): 
        print('connecting to network...')
        wifi.active(True) 
        while not wifi.isconnected():
            pass 
    print('network config:', wifi.ifconfig())
    selfadd=wifi.ifconfig()[0]

exec(open('config.py').read())
exec(open('config_s.py').read())   #加载舵机中位
led.value(1)        #网络加载完成，关闭LED
#=============一些中间或初始变量=============
t=0
init_x=0;init_y=-100
ges_x_1=0;ges_x_2=0;ges_x_3=0;ges_x_4=0
ges_y_1=init_y;ges_y_2=init_y;ges_y_3=init_y;ges_y_4=init_y
PIT_S=0;ROL_S=0;X_S=0;PIT_goal=0;ROL_goal=0;X_goal=0
spd=0;L=0;R=0
R_H=abs(init_y);H_goal=100
init_case=0
key_stab=False;gait_mode=0
stop_run_node=0

def cal_test_shank(x):
  p1=0.006649
  p2=0.4414
  p3=5.53
  return p1*x*x+p2*x+p3
  

def servo_output(case,init,ham1,ham2,ham3,ham4,shank1,shank2,shank3,shank4):
  if case==0 and init==0:
    #腿1
    PA_SERVO.angle(4, init_1h+90-ham1)  # 腿1大腿
    PA_SERVO.angle(5, (init_1s-90)+cal_test_shank(shank1))  # 腿1小腿
    #腿2
    PA_SERVO.angle(6,init_2h-90+ham2)  # 腿2大腿
    PA_SERVO.angle(7, (init_2s+90)-cal_test_shank(shank2))  # 腿2小腿
    #腿3
    PA_SERVO.angle(8, init_3h-90+ham3)  # 腿3大腿
    PA_SERVO.angle(9, (init_3s+90)-cal_test_shank(shank3))  # 腿3小腿
    #腿4
    PA_SERVO.angle(10, init_4h+90-ham4)  # 腿4大腿
    PA_SERVO.angle(11, (init_4s-90)+cal_test_shank(shank4))  # 腿4小腿
  else:
    #腿1
    PA_SERVO.angle(4, init_1h)  # 腿1大腿
    PA_SERVO.angle(5, init_1s)  # 腿1小腿
    #腿2
    PA_SERVO.angle(6, init_2h)  # 腿2大腿
    PA_SERVO.angle(7, init_2s)  # 腿2小腿
    #腿3
    PA_SERVO.angle(8, init_3h)  # 腿3大腿
    PA_SERVO.angle(9, init_3s)  # 腿3小腿
    #腿4
    PA_SERVO.angle(10, init_4h)  # 腿4大腿
    PA_SERVO.angle(11, init_4s)  # 腿4小腿



sitaa=0
def show_circle(times):
  global sitaa,stop_run_node
  for i in range(times):
    stop_run_node=1
    while True:
      h=50
      R=15
      PIT_C=atan(R*sin(sitaa)/h)*180/pi
      ROL_C=atan(R*cos(sitaa)/h)*180/pi
      if sitaa>=3.14*2:
        sitaa=0
        break
      else:
        sitaa=sitaa+0.1
      P_G=PA_ATTITUDE.cal_ges(PIT_C,ROL_C,l,b,w,X_S,R_H)
      ges_x_1=P_G[0];ges_x_2=P_G[1]; ges_x_3=P_G[2]; ges_x_4=P_G[3];ges_y_1=P_G[4];ges_y_2=P_G[5]; ges_y_3=P_G[6]; ges_y_4=P_G[7]
      A_=PA_IK.ik(ma_case,l1,l2,ges_x_1,ges_x_2,ges_x_3,ges_x_4,ges_y_1,ges_y_2,ges_y_3,ges_y_4)
      servo_output(ma_case,init_case,A_[0],A_[1],A_[2],A_[3],A_[4],A_[5],A_[6],A_[7])
  stop_run_node=0


def height(goal):    #高度调节函数
    global H_goal
    H_goal=goal

def gesture(PIT,ROL,X):
    global PIT_goal,ROL_goal,X_goal
    PIT_goal=PIT
    ROL_goal=ROL
    X_goal=X

#快速调节函数（适用于串口）
def g(PIT):
    global PIT_goal
    PIT_goal=PIT
    
def m(spd_,L_,R_):
    global spd,L,R
    spd=spd_;L=L_;R=R_
#快速调节函数（适用于串口）


def move(spd_,L_,R_):
    global spd,L,R
    spd=spd_;L=L_;R=R_
  
def stable(key):
    global key_stab
    key_stab=key
  
def servo_init(key):
    global init_case
    init_case=key
    
def gait(mode):   #设置步态
    global gait_mode
    gait_mode=mode
  


def mainloop():
    global t
    global R_H
    global PIT_S,ROL_S,X_S
    global ges_x_1,ges_x_2,ges_x_3,ges_x_4
    global ges_y_1,ges_y_2,ges_y_3,ges_y_4
    #锁定
    if stop_run_node==1:
      return 0
    #判断步态模式
    if gait_mode==0:
        if t>=(Ts-speed):#一个完整的运动周期结束 trot
            t=0
        elif L==0 and R==0:
            t=0
        else:
            t=t+speed
        #P_=PA_TROT.cal_t(t,-spd*4,spd*4,h,L,L,R,R)
        P_=PA_TROT.cal_t(t,0,spd*10,h,L,L,R,R)
    elif gait_mode==1:
        if t>=(Ts*2+0.5-walk_speed):#一个完整的运动周期结束 walk
            t=0
        elif L==0 and R==0:
            t=0
        else:
            pass    #pass,因为walk采用模块内自动加
        P_=PA_WALK.cal_w(CG_X,CG_Y,l,abs(spd)*7,walk_h,walk_speed,t,L,L,R,R)

    #高度调节器1
    if R_H>H_goal:
        R_H=R_H-abs(R_H-H_goal)*Kp_H
    elif R_H<H_goal:
        R_H=R_H+abs(R_H-H_goal)*Kp_H
    #姿态调节器
    if PIT_S>PIT_goal:   #俯仰
        PIT_S=PIT_S-abs(PIT_S-PIT_goal)*Kp_G
    elif PIT_S<PIT_goal:
        PIT_S=PIT_S+abs(PIT_S-PIT_goal)*Kp_G

    if ROL_S>ROL_goal:   #滚转
        ROL_S=ROL_S-abs(ROL_S-ROL_goal)*Kp_G
    elif ROL_S<ROL_goal:
        ROL_S=ROL_S+abs(ROL_S-ROL_goal)*Kp_G
          
    if X_S>X_goal:   #X位置
        X_S=X_S-abs(X_S-X_goal)*Kp_G
    elif X_S<X_goal:
        X_S=X_S+abs(X_S-X_goal)*Kp_G
    #姿态角度限位  
    if PIT_S>=pit_max_ang:PIT_S=pit_max_ang
    if PIT_S<=-pit_max_ang:PIT_S=-pit_max_ang
    if ROL_S>=rol_max_ang:ROL_S=rol_max_ang
    if ROL_S<=-rol_max_ang:ROL_S=-rol_max_ang
    #TROT模态根据迈腿长度自动调节重心
    if gait_mode==0:
        if spd>=0 and (L+R)!=0:
            P_G=PA_ATTITUDE.cal_ges(PIT_S,ROL_S,l,b,w,X_S-abs(spd)*trot_cg_f,R_H)
        elif spd<0 and (L+R)!=0:
            P_G=PA_ATTITUDE.cal_ges(PIT_S,ROL_S,l,b,w,X_S+abs(spd)*trot_cg_b,R_H)
        elif (L+R)==0:    #原地旋转
            P_G=PA_ATTITUDE.cal_ges(PIT_S,ROL_S,l,b,w,X_S+abs(spd)*trot_cg_t,R_H)
    else:
        P_G=PA_ATTITUDE.cal_ges(PIT_S,ROL_S,l,b,w,X_S,R_H)
    ges_x_1=P_G[0];ges_x_2=P_G[1]; ges_x_3=P_G[2]; ges_x_4=P_G[3];ges_y_1=P_G[4];ges_y_2=P_G[5]; ges_y_3=P_G[6]; ges_y_4=P_G[7]
    #自稳调节器（只静态稳定）:
    if spd==0 and L==0 and R==0 and key_stab==True:
        PA_STABLIZE.stab()
    #作动
    A_=PA_IK.ik(ma_case,l1,l2,P_[0]+ges_x_1,P_[1]+ges_x_2,P_[2]+ges_x_3,P_[3]+ges_x_4,P_[4]+ges_y_1,P_[5]+ges_y_2,P_[6]+ges_y_3,P_[7]+ges_y_4)
    servo_output(ma_case,init_case,A_[0],A_[1],A_[2],A_[3],A_[4],A_[5],A_[6],A_[7])

    

print("Py-apple V6.8 通用控制器 by 灯哥 2021214 ESP32)")
print("开源协议:Apache License 2.0")
print("作者邮件:ream_d@yeah.net")




