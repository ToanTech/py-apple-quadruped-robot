'''
Copyright Deng (ream_d@yeah.net)  Py-apple dog project

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

#===头===
#1==-==2
#4==-==3

def run_trot(r1,r4,r2,r3):    #小跑步态执行函数
    global t
    global x1,x2,x3,x4
    global y1,y2,y3,y4
    if t<=Ts*faai:
        sigma=2*pi*t/(faai*Ts)
        zep=h*(1-cos(sigma))/2
        xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs;
        xep_z=(xs-xf)*((sigma-sin(sigma))/(2*pi))+xf
        #输出y
        y1=ges_y_1+zep
        y2=ges_y_2
        y3=ges_y_3+zep
        y4=ges_y_4
        #输出x
        x1=-xep_z*r1
        x2=-xep_b*r2
        x3=-xep_z*r3
        x4=-xep_b*r4
    if t>Ts*faai and t<Ts:
        sigma=2*pi*(t-Ts*faai)/(faai*Ts)
        
        zep=h*(1-cos(sigma))/2;
        xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs;
        xep_z=(xs-xf)*((sigma-sin(sigma))/(2*pi))+xf
        #输出y
        y1=ges_y_1
        y2=ges_y_2+zep
        y3=ges_y_3
        y4=ges_y_4+zep
        #输出x
        x1=-xep_b*r1
        x2=-xep_z*r2
        x3=-xep_b*r3
        x4=-xep_z*r4
        #x1=0
        #x2=0
        #x3=0
        #x4=0
    print('=========')
    print('x1:',x1)
    print('x2:',x2)
    print('x3:',x3)
    print('x4:',x4)
    
    caculate()
    servo_output()
    
   
   
def trot(num):
    global t
    global x1,x2,x3,x4
    global y1,y2,y3,y4
    global xf,xs
    for i in range(abs(num)):
            while True: 
                if t>=Ts:#一个完整的运动周期结束
                    t=0
                    break
                else:
                    t=t+speed
                    if num>0:
                        run_trot(1,1,1,1)
                        xf=xf_f
                        xs=xf_b
                    elif num<0:
                        xf=xf_b
                        xs=xs_b
                        run_trot(-1,-1,-1,-1)
            print("-------------循环"+str(i+1)+"-------------")

    x1=0
    x2=0
    x3=0
    x4=0
    caculate()
    servo_output()

#===头===
#1==-==2
#4==-==3
def turn(num):
    global t
    global x1,x2,x3,x4
    global y1,y2,y3,y4
    global xf,xs
    for i in range(abs(num)):
            while True: 
                if t>=Ts:#一个完整的运动周期结束
                    t=0
                    break
                else:
                    t=t+speed
                    if num>0:     #左转
                        run_trot(-1,-1,1,1)
                        xf=xf_l
                        xs=xs_l
                    elif num<0:   #右转
                        xf=xf_r
                        xs=xs_r
                        run_trot(1,1,-1,-1)
            print("-------------循环"+str(i+1)+"-------------")

    x1=0
    x2=0
    x3=0
    x4=0
    caculate()
    servo_output()
