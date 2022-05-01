import padog
#padog.foot_init()

padog.height(40)
padog.height(120)
padog.height(40)
padog.height(120)

#姿态功能测试
padog.gesture(20,0)
padog.gesture(-20,0)
padog.gesture(0,0)
padog.gesture(0,25)
padog.gesture(0,-25)
padog.gesture(0,0)

#扭动功能测试
padog.show_circle(60,10)
padog.show_circle(50,10)
padog.show_circle(40,10)
padog.show_circle(30,10)
padog.show_circle(30,10)
padog.show_circle(30,10)
padog.show_circle(40,10)
padog.show_circle(50,10)
padog.show_circle(60,10)
padog.gesture(0,0)
"""
#跳跃功能测试
padog.start_jump(5)
"""
#直行功能测试
padog.trot(11)
padog.trot(-10)

#转弯功能测试
padog.turn(5)
padog.turn(-5)

#平移功能测试
padog.trans(5)
padog.trans(-5)
