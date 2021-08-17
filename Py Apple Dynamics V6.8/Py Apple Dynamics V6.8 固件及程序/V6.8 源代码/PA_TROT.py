#Copyright Deng（灯哥） (ream_d@yeah.net)  Py-apple dog project
#Github:https://github.com/ToanTech/py-apple-quadruped-robot
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file exchept in compliance with the License.
#You may obtain a copy of the License at:http://www.apache.org/licenses/LICENSE-2.0
from math import sin,cos,pi,atan,tan
from machine import I2C, Pin
import padog

#初始变量设置
faai=0.5
Ts=1

def cal_t(t,xs,xf,h,r1,r4,r2,r3):    #小跑步态执行函数
    global q,sita,cg_adjust

    if t<=Ts*faai:
        sigma=2*pi*t/(faai*Ts)
        zep=h*(1-cos(sigma))/2
        xep_z=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
        xep_b=(xs-xf)*((sigma-sin(sigma))/(2*pi))+xf
        #输出y
        y1=zep
        y2=0
        y3=zep
        y4=0
        #输出x
        x1=-xep_b*r1
        x2=-xep_z*r2
        x3=-xep_b*r3
        x4=-xep_z*r4

    elif t>Ts*faai and t<=Ts:
        sigma=2*pi*(t-Ts*faai)/(faai*Ts)
        zep=h*(1-cos(sigma))/2;
        xep_z=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
        xep_b=(xs-xf)*((sigma-sin(sigma))/(2*pi))+xf
        #输出y
        y1=0
        y2=zep
        y3=0
        y4=zep
        #输出x
        x1=-xep_z*r1
        x2=-xep_b*r2
        x3=-xep_z*r3
        x4=-xep_b*r4

    return x1,x2,x3,x4,y1,y2,y3,y4
