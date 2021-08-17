import padog
import socket
from math import floor
#-----------------------HTTP Server-----------------------#
user_leg_num="1"
url_cal="cal.html"
url_c="control.html"
thr=0;turn=0;L=0;R=0;Pitch=0;Roll=0;Yst=padog.in_y;Hgt=110 #中间变量定义
color_leg1='#7DFF7D';color_leg2='#FF9E9E';color_leg3='#FF9E9E';color_leg4='#FF9E9E';
test_add=0
url_n=url_c
g_s_num=100
addr = (padog.selfadd,80) #定义socket绑定的地址，ip地址为本地，端口为80
s = socket.socket()     #创建一个socket对象
s.bind(addr)            #绑定地址
s.listen(1)             #设置允许连接的客户端数量
print('listening on:', addr)
padog.gesture(Pitch,Roll,Yst)

while True:
  cl, addr = s.accept() #接受客户端的连接请求，cl为此链接创建的一个新的scoket对象，addr客户端地址
  #print('client connected from:', addr)
  req=str(cl.recv(1024))
  cl.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: FireBeetle\nContent-Type: text/html\n\n')
  req=req.split('\\r\\n')
  #http header 解析
  req_data=req[0].lstrip().rstrip().replace(' ','').lower()
  if req_data.find('favicon.ico')>-1:
    cl.close()
    continue
  else:
    req_data=req_data.replace('get/?','').replace('http/1.1','').replace("b'","")
    #print('req_data',req_data)
    if req_data.find('speed')>-1:
      print(req_data.replace('&',';'))
      exec(req_data.replace('&',';'))
      padog.l1=l1
      padog.l2=l2
      padog.l=l
      padog.b=b
      padog.w=w
      padog.speed=speed
      padog.h=h
      padog.Kp_H=kp_h
      padog.Kp_G=kp_g
      padog.CG_X=cg_x
      padog.CG_Y=cg_y
      padog.walk_h=walk_h
      padog.walk_speed=walk_speed
      padog.trot_cg_f=trot_cg_f
      padog.trot_cg_b=trot_cg_b
      padog.trot_cg_t=trot_cg_t
    #判断摇杆
    index_f = req_data.find('f=')
    index_find_t = req_data.find('t=')
    value_f = req_data[index_f+2:index_find_t].lstrip().rstrip()
    index_t = req_data.find('t=')
    value_t = req_data[index_t+2:index_t+6].lstrip().rstrip()
    try:
      thr=int(value_f)*6/100
      turn=int(value_t)
    except:
      pass
    #判断按钮
    index = req_data.find('key=')
    value = req_data[index+4:index+6].lstrip().rstrip()
    #Pitch
    if req_data.find('pit=')>-1:
      index_p = req_data.find('pit=')
      value_p = req_data[index_p+4:index_p+7].lstrip().rstrip()
      if value_p!='/':
        print('pit:',str(value_p))
        Pitch=int(value_p)
    #Roll
    if req_data.find('rol=')>-1:
      index_r = req_data.find('rol=')
      value_r = req_data[index_r+4:index_r+7].lstrip().rstrip()
      if value_r!='/':
        #print('rol:',str(value_r))
        Roll=int(value_r)
    #Height
    if req_data.find('hgt=')>-1:
      index_h = req_data.find('hgt=')
      value_h = req_data[index_h+4:index_h+7].lstrip().rstrip()
      if value_h!='/':
        print('hgt:',str(value_h))
        Hgt=int(value_h)
    #Y_controller
    if req_data.find('yst=')>-1:
      index_y = req_data.find('yst=')
      value_y = req_data[index_y+4:index_y+7].lstrip().rstrip()
      if value_y!='/':
        print('yst:',str(value_y))
        Yst=int(value_y)
    #运动控制用
    elif value == 'ss':
      Pitch=0;Roll=0          #清除姿态
      padog.stable(False)     #清除陀螺仪
      padog.gait(0)           #重置步态模式
      url_n=url_cal
    elif value == 'go':
      print('True')
      padog.stable(True)
    elif value == 'gc':
      print('False')
      padog.stable(False)
    elif value == 'g0':
      padog.stable(False)   #切换walk步态时自动关闭陀螺仪，防止冲突
      padog.gait(0)
    elif value == 'g1':
      padog.stable(False)
      padog.gait(1)
    #标定判断用
    if value == 'l2':
      user_leg_num='2'
      color_leg1='#FF9E9E';color_leg2='#7DFF7D';color_leg3='#FF9E9E';color_leg4='#FF9E9E'
    elif value == 'l4':
      user_leg_num='4'
      color_leg1='#FF9E9E';color_leg2='#FF9E9E';color_leg3='#FF9E9E';color_leg4='#7DFF7D'
    elif value == 'l1':
      user_leg_num='1'
      color_leg1='#7DFF7D';color_leg2='#FF9E9E';color_leg3='#FF9E9E';color_leg4='#FF9E9E'
    elif value == 'l3':
      user_leg_num='3'
      color_leg1='#FF9E9E';color_leg2='#FF9E9E';color_leg3='#7DFF7D';color_leg4='#FF9E9E'
    elif value == 'sc':   #保存并退出
      s_f = open("config_s.py", "w+")
      #保存中位
      s_f.write("init_1h="+str(padog.init_1h)+"\n")
      s_f.write("init_1s="+str(padog.init_1s)+"\n")
      s_f.write("init_2h="+str(padog.init_2h)+"\n")
      s_f.write("init_2s="+str(padog.init_2s)+"\n")
      s_f.write("init_3h="+str(padog.init_3h)+"\n")
      s_f.write("init_3s="+str(padog.init_3s)+"\n")
      s_f.write("init_4h="+str(padog.init_4h)+"\n")
      s_f.write("init_4s="+str(padog.init_4s)+"\n")
      #保存机械、步态参数
      s_f.write("l1="+str(padog.l1)+"\n")
      s_f.write("l2="+str(padog.l2)+"\n")
      s_f.write("l="+str(padog.l)+"\n")
      s_f.write("b="+str(padog.b)+"\n")
      s_f.write("w="+str(padog.w)+"\n")
      s_f.write("speed="+str(padog.speed)+"\n")
      s_f.write("h="+str(padog.h)+"\n")
      s_f.write("Kp_H="+str(padog.Kp_H)+"\n")
      s_f.write("Kp_G="+str(padog.Kp_G)+"\n")
      s_f.write("CG_X="+str(padog.CG_X)+"\n")
      s_f.write("CG_Y="+str(padog.CG_Y)+"\n")
      s_f.write("walk_h="+str(padog.walk_h)+"\n")
      s_f.write("walk_speed="+str(padog.walk_speed)+"\n")
      s_f.write("ma_case="+str(padog.ma_case)+"\n")
      s_f.write("trot_cg_f="+str(padog.trot_cg_f)+"\n")
      s_f.write("trot_cg_b="+str(padog.trot_cg_b)+"\n")
      s_f.write("trot_cg_t="+str(padog.trot_cg_t)+"\n")
      #保存重心平移量
      s_f.write("in_y="+str(Yst)+"\n")
      s_f.close()      
      url_n=url_c
      padog.servo_init(0)
            
    elif value == 'hi':
      exec("padog.init_"+user_leg_num+"h="+"padog.init_"+user_leg_num+"h+1")
    elif value == 'hd':
      exec("padog.init_"+user_leg_num+"h="+"padog.init_"+user_leg_num+"h-1")
    elif value == 'si':
      exec("padog.init_"+user_leg_num+"s="+"padog.init_"+user_leg_num+"s+1")
    elif value == 'sd':
      exec("padog.init_"+user_leg_num+"s="+"padog.init_"+user_leg_num+"s-1")
    elif value == 't9':
      padog.servo_init(1)
      
  with open(url_n, 'r') as f:
    while(req_data.find('speed')>-1 or (req_data.find('f=')==-1 and req_data.find('g0')==-1 and req_data.find('g1')==-1 and req_data.find('go')==-1 and req_data.find('gc')==-1 and req_data.find('pit=')==-1 and req_data.find('rol=')==-1 and req_data.find('yst=')==-1 and req_data.find('hgt=')==-1)):
      out=f.read(1300)
      if out:
        try:
          cl.sendall(out)
        except:pass
      else:
        #返回此时控制器初始设定值
        try:
          cl.sendall("""
        <script type="text/javascript">
        dimSlide3.value="""+str(Yst)+"""
        </script>
        """)
        except:pass
        break
      #test_add=test_add+1
      #print('Gogo:',test_add)
    if url_n=="cal.html":
      try:
        cl.sendall("""
      <center><table border="3">
      <tr>
      <th bgcolor='"""+color_leg1+"""'>1号大腿："""+str(padog.init_1h)+"""<Br/>1号小腿："""+str(padog.init_1s)+"""</th>
      <th bgcolor='"""+color_leg2+"""'>2号大腿："""+str(padog.init_2h)+"""<Br/>2号小腿："""+str(padog.init_2s)+"""</th>
      </tr>
      <tr>
      <th bgcolor='"""+color_leg4+"""'>4号大腿："""+str(padog.init_4h)+"""<Br/>4号小腿："""+str(padog.init_4s)+"""</th>
      <th bgcolor='"""+color_leg3+"""'>3号大腿："""+str(padog.init_3h)+"""<Br/>3号小腿："""+str(padog.init_3s)+"""</th>
      </tr>
      </table></center><Br/><Br/>
      """)
      
        cl.sendall("""
            <center>
            <h1>控制器参数设定</h1>
            <br />
            <br />
            <form action="/" method="get" accept-charset="utf-8">
            """+
            """<br /><p>大腿(杆1)长　　　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="l1" """+"""value='"""+str(padog.l1)+"""'/></p>"""+\
            """<br /><p>小腿(杆2)长　　　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="l2" """+"""value='"""+str(padog.l2)+"""'/></p>"""+\
            """<br /><p>机器人长度　　 　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="l" """+"""value='"""+str(padog.l)+"""'/></p>"""+\
            """<br /><p>机器人宽度　　 　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="b" """+"""value='"""+str(padog.b)+"""'/></p>"""+\
            """<br /><p>机器人腿间距 　　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="w" """+"""value='"""+str(padog.w)+"""'/></p>"""+\
            """<br /><p>TROT步态步频　　　　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="speed" """+"""value='"""+str(padog.speed)+"""'/></p>"""+\
            """<br /><p>TROT抬腿高度　　　　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="h" """+"""value='"""+str(padog.h)+"""'/></p>"""+\
            """<br /><p>TROT前进重心调整P　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="trot_cg_f" """+"""value='"""+str(padog.trot_cg_f)+"""'/></p>"""+\
            """<br /><p>TROT后退重心调整P　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="trot_cg_b" """+"""value='"""+str(padog.trot_cg_b)+"""'/></p>"""+\
            """<br /><p>TROT转向重心调整P　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="trot_cg_t" """+"""value='"""+str(padog.trot_cg_t)+"""'/></p>"""+\

            """<br /><p>WALK步态抬腿高度　　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="walk_h" """+"""value='"""+str(padog.walk_h)+"""'/></p>"""+\
            """<br /><p>WALK步态步频　　　　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="walk_speed" """+"""value='"""+str(padog.walk_speed)+"""'/></p>"""+\
            """<br /><p>高度调节P环　　　　　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="Kp_H" """+"""value='"""+str(padog.Kp_H)+"""'/></p>"""+\
            """<br /><p>姿态调节P环　　　　　:&nbsp;<input type="text"  style="width:100px; height:30px;" name="Kp_G" """+"""value='"""+str(padog.Kp_G)+"""'/></p>"""+\
            """<br /><p>X方向重心偏移量　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="CG_X" """+"""value='"""+str(padog.CG_X)+"""'/></p>"""+\
            """<br /><p>Y方向重心偏移量　　   :&nbsp;<input type="text"  style="width:100px; height:30px;" name="CG_Y" """+"""value='"""+str(padog.CG_Y)+"""'/></p>"""+\
            """<br /><input type="Submit" style="width:100px; height:30px;" value="更改控制器参数"  />  """+\
            """</form>
            </center>
            </body>
            </html>
            """)
      except:pass
  cl.close()          #关闭socket

  #命令
  if thr>=6:
    thr=6
  elif thr<=-3:
    thr=-3
     
  if turn>=80:
    L=1;R=-1;thr=2
  elif turn<=-80:
    L=-1;R=1;thr=2
  else:
    L=1;R=1

  if thr==0:
    padog.move(0,0,0)
  else:
    padog.move(thr,L,R)

  padog.height(Hgt)
  padog.gesture(Pitch,Roll,Yst)





