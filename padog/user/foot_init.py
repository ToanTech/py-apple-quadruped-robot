def init_servo_mov():
    global init_1h,init_1s,init_2h,init_2s,init_3h,init_3s,init_4h,init_4s
    #print(init_1s)
    #腿1
    servos.position(4, degrees=init_1h)  # 腿1大腿
    servos.position(5, degrees=init_1s)  # 腿1小腿
    #腿2
    servos.position(6, degrees=init_2h)  # 腿2大腿
    servos.position(7, degrees=init_2s)  # 腿2小腿
    #腿3
    servos.position(8, degrees=init_3h)  # 腿3大腿
    servos.position(9, degrees=init_3s)  # 腿3小腿
    #腿4
    servos.position(10, degrees=init_4h)  # 腿4大腿
    servos.position(11, degrees=init_4s)  # 腿4小腿

#===头===
#1==-==2
#4==-==3
def foot_init():
    global init_1h,init_1s,init_2h,init_2s,init_3h,init_3s,init_4h,init_4s
    print("PY-APPLE DOG 菠萝狗辅助脚调中系统")
    print("==================================")
    init_servo_mov()
    while True:
        print("#方向")
        print("#===头===")
        print("#1==-==2")
        print("#4==-==3")
        user_leg_num=input("请输入腿号【按q并回车退出调平】>>")
        if user_leg_num=="q":
            print("=============调中结果=============")
            print("init_1h:",init_1h)
            print("init_1s:",init_1s)
            print("init_2h:",init_2h)
            print("init_2s:",init_2s)
            print("init_3h:",init_3h)
            print("init_3s:",init_3s)
            print("init_4h:",init_4h)
            print("init_4s:",init_4s)
            print("=============调中结果=============")
            break
        else:
            while True:
                init_servo_mov()
                user_leg_die=input("请输入调平方向并回车【+/-/q(退出)】>>")
                exec("print(init_"+user_leg_num+")")
                if user_leg_die=="+":
                    exec("init_"+user_leg_num+"="+"init_"+user_leg_num+"+1")
                    #try:
                    #    exec("init_"+user_leg_num+"="+"init_"+user_leg_num+"+1")
                    #except:
                    #    print("请检查是否有输入错误")
                elif user_leg_die=="-":
                    try:
                        exec("padog.init_"+user_leg_num+"="+"padog.init_"+user_leg_num+"-1")
                    except:
                        print("请检查是否有输入错误")
                elif user_leg_die=="q":
                    break
        