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
R_H=abs(init_y)   #初始高度与init_y相同
PIT_S=0
ROL_S=0

#gesture 姿态控制部分
#机体参数设定

Hc=abs(init_y)
b = 105   #机器人宽度
w = 132   #机器人腿间距
l = 202   #机器人长度
def cal_gesture(PIT,ROL):
    global x1,x2,x3,x4
    global y1,y2,y3,y4
    global ges_x_1,ges_x_2,ges_x_3,ges_x_4
    global ges_y_1,ges_y_2,ges_y_3,ges_y_4
    YA=0
    P=PIT*pi/180
    R=ROL*pi/180
    Y=YA*pi/180
    #左前
    ABl_x=l/2 - (l*cos(P)*cos(Y))/2 + (b*cos(P)*sin(Y))/2
    ABl_y=w/2 - (b*(cos(R)*cos(Y) + sin(P)*sin(R)*sin(Y)))/2 - (l*(cos(R)*sin(Y) - cos(Y)*sin(P)*sin(R)))/2
    ABl_z= - Hc - (b*(cos(Y)*sin(R) - cos(R)*sin(P)*sin(Y)))/2 - (l*(sin(R)*sin(Y) + cos(R)*cos(Y)*sin(P)))/2
    '''
    print("ABl_x:",ABl_x)
    print("ABl_y:",ABl_y)
    print("ABl_z:",ABl_z)
    print("=====")
    '''
    #右前
    AB2_x=l/2 - (l*cos(P)*cos(Y))/2 - (b*cos(P)*sin(Y))/2
    AB2_y=(b*(cos(R)*cos(Y) + sin(P)*sin(R)*sin(Y)))/2 - w/2 - (l*(cos(R)*sin(Y) - cos(Y)*sin(P)*sin(R)))/2
    AB2_z=(b*(cos(Y)*sin(R) - cos(R)*sin(P)*sin(Y)))/2 - Hc - (l*(sin(R)*sin(Y) + cos(R)*cos(Y)*sin(P)))/2
    '''
    print("AB2_x:",AB2_x)
    print("AB2_y:",AB2_y)
    print("AB2_z:",AB2_z)
    print("=====")
    '''
    #左后
    AB3_x=(l*cos(P)*cos(Y))/2 - l/2 + (b*cos(P)*sin(Y))/2
    AB3_y=w/2 - (b*(cos(R)*cos(Y) + sin(P)*sin(R)*sin(Y)))/2 + (l*(cos(R)*sin(Y) - cos(Y)*sin(P)*sin(R)))/2
    AB3_z=(l*(sin(R)*sin(Y) + cos(R)*cos(Y)*sin(P)))/2 - (b*(cos(Y)*sin(R) - cos(R)*sin(P)*sin(Y)))/2 - Hc
    '''
    print("AB3_x:",AB3_x)
    print("AB3_y:",AB3_y)
    print("AB3_z:",AB3_z)
    print("=====")
    '''
    #右后
    AB4_x=(l*cos(P)*cos(Y))/2 - l/2 - (b*cos(P)*sin(Y))/2
    AB4_y=(b*(cos(R)*cos(Y) + sin(P)*sin(R)*sin(Y)))/2 - w/2 + (l*(cos(R)*sin(Y) - cos(Y)*sin(P)*sin(R)))/2
    AB4_z=(b*(cos(Y)*sin(R) - cos(R)*sin(P)*sin(Y)))/2 - Hc + (l*(sin(R)*sin(Y) + cos(R)*cos(Y)*sin(P)))/2
    '''
    print("AB4_x:",AB4_x)
    print("AB4_y:",AB4_y)
    print("AB4_z:",AB4_z)
    print("=====")
    '''

    #======舵机输出======
    #狗腿子顺序(从1开始顺时针数)
    #===头===
    #1(AB1)==-==2(AB2)
    #4(AB3)==-==3(AB4)
    x1=ABl_x
    y1=ABl_z

    x2=AB2_x
    y2=AB2_z

    x3=AB4_x
    y3=AB4_z

    x4=AB3_x
    y4=AB3_z


    ges_x_1=ABl_x
    ges_x_2=AB2_x
    ges_x_3=AB4_x
    ges_x_4=AB3_x

    ges_y_1=ABl_z
    ges_y_2=AB2_z
    ges_y_3=AB4_z
    ges_y_4=AB3_z
    caculate()
    servo_output()

def gesture(PIT_goal,ROL_goal):
    global PIT_S,ROL_S
    
    while True:
        if PIT_S>PIT_goal:
            PIT_S=PIT_S-abs(PIT_S-PIT_goal)*Kp_G
        elif PIT_S<PIT_goal:
            PIT_S=PIT_S+abs(PIT_S-PIT_goal)*Kp_G

        if ROL_S>ROL_goal:
            ROL_S=ROL_S-abs(ROL_S-ROL_goal)*Kp_G
        elif ROL_S<ROL_goal:
            ROL_S=ROL_S+abs(ROL_S-ROL_goal)*Kp_G
        if abs(PIT_S-PIT_goal)<0.1 and abs(ROL_S-ROL_goal)<0.1 :
            break
        cal_gesture(PIT_S,ROL_S)

#4条腿坐标同时调节
def control_4_legs(x,y):
    global y1,y2,y3,y4
    global x1,x2,x3,x4
    y1 = -y
    y2 = -y
    y3 = -y
    y4 = -y
    x1=x
    x2=x
    x3=x
    x4=x
    

    
    caculate()
    servo_output()
def control_f(x,y):
    global y1,y2,y3,y4
    global x1,x2,x3,x4
    y1 = -y
    y2 = -y
    x1=x
    x2=x

    
    caculate()
    servo_output()
#高度调节函数
def height(goal):
    global y1,y2,y3,y4
    global x1,x2,x3,x4
    global R_H
    global ges_y_1,ges_y_2,ges_y_3,ges_y_4
    while True:
        if R_H>goal:
            R_H=R_H-abs(R_H-goal)*Kp_H
        elif R_H<goal:
            R_H=R_H+abs(R_H-goal)*Kp_H
        if abs(R_H-goal)<1:
            break
        print("高度坐标",R_H)
        y1 = -R_H
        y2 = -R_H
        y3 = -R_H
        y4 = -R_H
        
        ges_y_1 = -R_H
        ges_y_2 = -R_H
        ges_y_3 = -R_H
        ges_y_4 = -R_H
        x1=0
        x2=0
        x3=0
        x4=0

    
        caculate()
        servo_output()


sita=0
Kp_G_S=0
def show_circle(h,R):
    global sita
    global Kp_G
    Kp_G_S=Kp_G
    Kp_G=0.6
    sita=0
    while(True):
        sita=sita+0.1
        ROL_C=atan(R*cos(sita)/h)*180/pi
        PIT_C=atan(R*sin(sita)/h)*180/pi
        #print("PIT",PIT_C)
        #print("ROL",ROL_C)
        gesture(PIT_C,ROL_C)
        if sita>=3.14*2:
            break
    Kp_G=Kp_G_S