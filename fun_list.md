# **菠萝狗**

## 函数表

函数表对应软件版本：<u>PADOG V0.1.01 BETA 2 2020417</u>

运行：在运行时，请先引入padog模块

```
import padog
```



##### padog.start_test(num)

踏步测试，其中的 num 是踏步步数



##### padog.height(goal)

高度调节函数，goal 是目标高度，单位mm。

（这个得在运动参数，比如腿长设置正确才会正常）



##### **padog.control_4_legs(x,y)**

同时控制四条腿的足端坐标值x,y（单位mm），可以让四条腿同时做动作