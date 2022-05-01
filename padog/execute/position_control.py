
#======运动学逆解======
def caculate():

    global x1,y1,x2,y2,x3,y3,x4,y4
    global ham1,ham2,ham3,ham4
    global shank1,shank2,shank3,shank4
    #腿1
    x1=-x1
    shank1=pi-acos((x1*x1+y1*y1-l1*l1-l2*l2)/(-2*l1*l2))
    fai1=acos((l1*l1+x1*x1+y1*y1-l2*l2)/(2*l1*sqrt(x1*x1+y1*y1)))
    if x1>0:
        ham1=abs(atan(y1/x1))-fai1
    elif x1<0:
        ham1=pi-abs(atan(y1/x1))-fai1
    else:
        ham1=pi-1.5707-fai1
    shank1=180*shank1/pi
    ham1=180*ham1/pi
    '''
    print('ham1:',ham1)
    print('shank1:',shank1)
    '''
    #腿2
    x2=-x2
    shank2=pi-acos((x2*x2+y2*y2-l1*l1-l2*l2)/(-2*l1*l2))
    fai2=acos((l1*l1+x2*x2+y2*y2-l2*l2)/(2*l1*sqrt(x2*x2+y2*y2)))
    if x2>0:
        ham2=abs(atan(y2/x2))-fai2
    elif x2<0:
        ham2=pi-abs(atan(y2/x2))-fai2
    else:
        ham2=pi-1.5707-fai2
    shank2=180*shank2/pi
    ham2=180*ham2/pi
    '''
    print('ham2:',ham2)
    print('shank2:',shank2)
    '''
    #腿3
    x3=-x3
    shank3=pi-acos((x3*x3+y3*y3-l1*l1-l2*l2)/(-2*l1*l2))
    fail3=acos((l1*l1+x3*x3+y3*y3-l2*l2)/(2*l1*sqrt(x3*x3+y3*y3)))
    if x3>0:
        ham3=abs(atan(y3/x3))-fail3
    elif x3<0:
        ham3=pi-abs(atan(y3/x3))-fail3
    else:
        ham3=pi-1.5707-fail3
    shank3=180*shank3/pi
    ham3=180*ham3/pi
    '''
    print('ham3:',ham3)
    print('shank3:',shank3)
    '''
    #腿4
    x4=-x4
    shank4=pi-acos((x4*x4+y4*y4-l1*l1-l2*l2)/(-2*l1*l2))
    fai4=acos((l1*l1+x4*x4+y4*y4-l2*l2)/(2*l1*sqrt(x4*x4+y4*y4)))
    if x4>0:
        ham4=abs(atan(y4/x4))-fai4
    elif x4<0:
        ham4=pi-abs(atan(y4/x4))-fai4
    else:
        ham4=pi-1.5707-fai4
    shank4=180*shank4/pi
    ham4=180*ham4/pi
    '''
    print('ham4:',ham4)
    print('shank4:',shank4)
    '''
#======舵机输出======
#狗腿子顺序(从1开始顺时针数)
#===头===
#1==-==2
#4==-==3
def servo_output():
    if ma_case==0:     #标准舵机正装
        #腿1
        servos.position(4, degrees=init_1h-ham1)  # 腿1大腿
        servos.position(5, degrees=(init_1s-90)+shank1)  # 腿1小腿
        #腿2
        servos.position(6, degrees=init_2h+ham2)  # 腿2大腿
        servos.position(7, degrees=(init_2s+90)-shank2)  # 腿2小腿
        #腿3
        servos.position(8, degrees=init_3h+ham3)  # 腿3大腿
        servos.position(9, degrees=(init_3s+90)-shank3)  # 腿3小腿
        #腿4
        servos.position(10, degrees=init_4h-ham4)  # 腿4大腿
        servos.position(11, degrees=(init_4s-90)+shank4)  # 腿4小腿
    elif ma_case==1:   #舵机侧装
        #腿1
        servos.position(4, degrees=init_1h-ham1)  # 腿1大腿
        servos.position(5, degrees=(init_1s+90)-shank1)  # 腿1小腿
        #腿2
        servos.position(6, degrees=init_2h+ham2)  # 腿2大腿
        servos.position(7, degrees=(init_2s-90)+shank2)  # 腿2小腿
        #腿3
        servos.position(8, degrees=init_3h+ham3)  # 腿3大腿
        servos.position(9, degrees=(init_3s-90)+shank3)  # 腿3小腿
        #腿4
        servos.position(10, degrees=init_4h-ham4)  # 腿4大腿
        servos.position(11, degrees=(init_4s+90)-shank4)  # 腿4小腿

