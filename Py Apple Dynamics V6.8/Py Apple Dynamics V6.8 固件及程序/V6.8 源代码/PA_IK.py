#Copyright Deng（灯哥） (ream_d@yeah.net)  Py-apple dog project
#Github:https://github.com/ToanTech/py-apple-quadruped-robot
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at:http://www.apache.org/licenses/LICENSE-2.0

from math import asin,acos,atan,pi,sqrt

def ik(case,l1,l2,x1,x2,x3,x4,y1,y2,y3,y4):
    if case==0:
      #=============串联腿=============
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
      
      return ham1,ham2,ham3,ham4,shank1,shank2,shank3,shank4
    #=============并连腿=============
    elif case==1:
      #腿1
      y1=-y1
      L1=sqrt(x1*x1+y1*y1)
      psai1=asin(x1/L1)
      fai1=acos((L1*L1+l1*l1-l2*l2)/(2*l1*L1))
      sita1_1=180*(fai1-psai1)/pi
      sita2_1=180*(fai1+psai1)/pi
      #腿2
      #x2=0
      #y2=71
      y2=-y2
      L2=sqrt(x2*x2+y2*y2)
      psai2=asin(x2/L2)
      fai2=acos((L2*L2+l1*l1-l2*l2)/(2*l1*L2))
      sita1_2=180*(fai2-psai2)/pi
      sita2_2=180*(fai2+psai2)/pi
      #腿3
      #x3=0
      #y3=71
      y3=-y3
      L3=sqrt(x3*x3+y3*y3)
      psai3=asin(x3/L3)
      fai3=acos((L3*L3+l1*l1-l2*l2)/(2*l1*L3))
      sita1_3=180*(fai3-psai3)/pi
      sita2_3=180*(fai3+psai3)/pi
      #腿4
      y4=-y4
      L4=sqrt(x4*x4+y4*y4)
      psai4=asin(x4/L4)
      fai4=acos((L4*L4+l1*l1-l2*l2)/(2*l1*L4))
      sita1_4=180*(fai4-psai4)/pi
      sita2_4=180*(fai4+psai4)/pi
      
      return sita1_1,sita1_2,sita1_3,sita1_4,sita2_1,sita2_2,sita2_3,sita2_4






