# **菠萝狗**

## 函数表

函数表对应软件版本：<u>PADOG V0.1.02 BETA 1 2020423</u>

运行：在运行时，请先引入padog模块

```
import padog
```



##### padog.trot(num)

小跑步态，其中的 num 是小跑步数，num>0 往前，num<0 往后



##### padog.height(goal)

高度调节函数，goal 是目标高度，单位mm。

（这个得在运动参数，比如腿长设置正确才会正常）



##### **padog.control_4_legs(x,y)**

同时控制四条腿的足端坐标值x,y（单位mm），可以让四条腿同时做动作