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
def trans(num):
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
                        gesture(0,10)
                        run_trot(1,1,1,1)
                        xf=0
                        xs=0

                    elif num<0:
                        xf=0
                        xs=0
                        gesture(0,-10)
                        run_trot(1,1,1,1)

    x1=0
    x2=0
    x3=0
    x4=0
    
    caculate()
    servo_output()
    gesture(0,0)