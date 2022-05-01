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
from math import *
#from machine import I2C
#from pyb import UART
#from pyb import Pin
import time
#import _thread

#==============版本信息==================#
version="V1.1 BETA 1 2020506"

#打印版本信息
print("=============================")
print("PY-APPLE DOG TEST VER "+version)
print("=============================")
print("作者：灯哥  ream_d@yeah.net    开源协议：Apache License")
print("=========实现功能=========")
print("1、踏步 2、高度调节 3、小跑基础版（向前、向后）4、分别调节各腿高度")
print("=========实现功能=========")

print("加载程序...")
Init_File_List=[".//padog//config.py",".//padog//user//foot_init.py",".//padog//execute//servo.py",".//padog//execute//position_control.py",".//padog//gait//trot.py",".//padog//gait//trans.py",".//padog//gait//jump.py",".//padog//gait//gesture_control.py"]

#调试使用
for i in Init_File_List:
    exec(open(i).read())
    print(i)

print("程序加载完成...")


#预先执行函数
caculate()
servo_output()