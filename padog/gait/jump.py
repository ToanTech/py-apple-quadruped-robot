#本程序参照 Stanford doggo jump 程序进行编写，感谢 Stanford doggo 项目及作者
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

def jump():
    global x1,x2,x3,x4
    global y1,y2,y3,y4
    if t < prep_time:  

        control_4_legs(x_jump,stance_height)
        print('Prep,y='+str(stance_height))

    elif t >= prep_time and t < (prep_time + launch_time):  #起跳

        control_4_legs(x_jump,jump_extension)
        print('Jumpping...,y='+str(jump_extension))

    elif t >= (prep_time + launch_time) and t < (prep_time + launch_time + fall_time):  #收腿待缓冲

        control_4_legs(x_jump,fall_extension)
        print('Falling...,y='+str(fall_extension))

   
   
def start_jump(num):
    global t
    for i in range(num):
            while True: 
                if t>=(prep_time + launch_time + fall_time):#一个完整的运动周期结束
                    t=0
                    break
                else:
                    t=t+0.035
                    jump()
            print("-------------循环"+str(i+1)+"-------------")
                    