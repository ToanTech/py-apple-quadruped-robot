#Copyright Deng（灯哥） (ream_d@yeah.net)  Py-apple dog project
#Github:https://github.com/ToanTech/py-apple-quadruped-robot
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at:http://www.apache.org/licenses/LICENSE-2.0
import PA_IMU
import PA_AVGFILT
import array
from machine import I2C, Pin
import padog

#中间变量定义
q=[]
Sta_Pitch=0
Sta_Roll=0
kp_sta=0.05
p_origin=0
r_origin=0
time_p=0
#设置陀螺仪 IIC 接口
try:
  i2cc = I2C(scl=Pin(22), sda=Pin(21))   #集成板
  acc = PA_IMU.accel(i2cc)
  acc.error_gy()
except:
  i2cc = I2C(scl=Pin(32), sda=Pin(33))   #直插板
  acc = PA_IMU.accel(i2cc)
  acc.error_gy()

#滑动平均滤波
#Pitch
gyro_data_p = array.array('i', [0]*5)
f_gyro_data_p = PA_AVGFILT.avg_filiter(gyro_data_p)
#Roll
gyro_data_r = array.array('i', [0]*5)
f_gyro_data_r = PA_AVGFILT.avg_filiter(gyro_data_r)

def stab():
  global q,Sta_Pitch,Sta_Roll,time_p,p_origin,r_origin
  ay=acc.get_values()
  
  if time_p<=50:
    try:
      p_origin=round(q[1])
      r_origin=round(q[2])
      time_p=time_p+1
    except:
      pass
  else:
    try:
      filter_data_p = f_gyro_data_p.avg(round(q[1]))
      #print('avg_filter_P:',filter_data)
      Sta_Pitch=Sta_Pitch-(filter_data_p-p_origin)*kp_sta
      if Sta_Pitch>=padog.pit_max_ang: 
        Sta_Pitch=padog.pit_max_ang
      elif Sta_Pitch<=-padog.pit_max_ang: 
        Sta_Pitch=-padog.pit_max_ang
    except:
      pass

    try:
      #print('R:',q[2])
      filter_data_r = f_gyro_data_r.avg(round(q[2]))
      Sta_Roll=Sta_Roll-(filter_data_r-r_origin)*kp_sta

      if Sta_Roll>=padog.rol_max_ang: 
        Sta_Roll=padog.rol_max_ang
      elif Sta_Roll<=-padog.rol_max_ang:
        Sta_Roll=-padog.rol_max_ang     
    except:
      pass
      
    padog.PIT_goal=Sta_Pitch
    padog.ROL_goal=Sta_Roll
   

  q=PA_IMU.IMUupdate(ay["GyX"]/65.5*0.0174533,ay["GyY"]/65.5*0.0174533,ay["GyZ"]/65.5*0.0174533,ay["AcX"]/8192,ay["AcY"]/8192,ay["AcZ"]/8192)




