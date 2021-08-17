import _thread
import padog
import time
from machine import Timer
from machine import UART
from padog import g,m
#
from machine import time_pulse_us
from machine import Pin


#run_mode=0：web遥控模式
#run_mode=1：OpenMV 巡线模式
#run_mode=2：OpenMV 颜色识别模式
#run_mode=3：调试模式

run_mode=0

uart6=UART(2,115200)
t = Timer(1)

def OpenMV_Run(t):
  command=""
  if uart6.any():
    read = uart6.read(1).decode('gbk')
    while read != '/':
      command = command + read
      read = uart6.read(1).decode('gbk')
    if(command != "1/" ) and command!="":
      try:
        exec(command)
        print("exec:",command)
      except:
        print("execerr:",command)
    command = ""


def app_1():
  exec(open('web_c.py').read())
  
def app_2():
  try:
    exec(open('my_code.py').read())
  except:
    print('积木编程代码执行出错，跳过...')
    
    
def serial_run_loop():
  while True:
    padog.mainloop()

def loop(t):
  padog.mainloop()
  

#模式判定
if run_mode==0:
  _thread.start_new_thread(app_1, ())
  t.init(period=10,mode=Timer.PERIODIC,callback=loop)
elif run_mode==1:
  t.init(period=50,mode=Timer.PERIODIC,callback=OpenMV_Run)
  padog.gesture(padog.in_pit,padog.in_rol,padog.in_y)
  padog.speed=0.045
  serial_run_loop()
elif run_mode==2:
  t.init(period=10,mode=Timer.PERIODIC,callback=OpenMV_Run)
  padog.gesture(padog.in_pit,padog.in_rol,padog.in_y)
  padog.speed=0.045
  serial_run_loop()
elif run_mode==3:
  _thread.start_new_thread(app_1, ())
  serial_run_loop()
