# **菠萝狗**

## 函数表

<u>函数表对应软件版本：PADOG V2.0  官方程序 2020525</u>

运行：在运行时，请先引入padog模块

```
import padog
```



##### 1. padog.trot(num)

小跑步态，其中的 num 是小跑步数，num>0 往前，num<0 往后

```
#trot例程
import padog
padog.trot(10)    #往前小跑十步
padog.trot(-10)   #往后小跑十步
```

##### 2. padog.height(goal)

高度调节函数，goal 是目标高度，单位mm。

```
#height例程
import padog
padog.height(100) #调节高度到100mm
padog.height(80)   #调节高度到80mm
```

##### **3. padog.control_4_legs(x,y)**

同时控制四条腿的足端坐标值x,y（单位mm），可以让四条腿同时做动作

```
#control_4_legs(x,y)例程
import padog
padog.control_4_legs(30,100)  #四条腿都同时设置到坐标(30，100)
```

#------以下函数将在20205525版本开放

**4. padog.turn(num)**

机器人原地自转，num为步数

```
#turn例程
import padog
padog.turn(10)  #往右自转十步
padog.turn(-10) #往左自转十步
```

**5. padog.trans(num)**

机器人平移，num为步数

```
#turn例程
import padog
padog.trans(10)  #往右平移十步
padog.trans(-10) #往左平移十步
```

**6. padog.trans(num)**

机器人平移，num为步数

```
#turn例程
import padog
padog.trans(10)  #往右平移十步
padog.trans(-10) #往左平移十步
```

**7. padog.gesture(PIT_goal,ROL_goal)**

机器人姿态设置，PIT_goal 为 Pitch 俯仰轴姿态调定目标；ROL_goal 为 Roll 滚转轴姿态调定目标

#gesture例程
import padog
padog.gesture(10,-10)  #仰头10度，负方向（左）滚转10度

**8. padog.foot_init()**

机器人腿部校准系统，具体使用方法见视频：（...待添加...）