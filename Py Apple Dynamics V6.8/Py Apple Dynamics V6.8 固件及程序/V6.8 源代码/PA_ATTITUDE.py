#Copyright Deng（灯哥） (ream_d@yeah.net)  Py-apple dog project
#Github:https://github.com/ToanTech/py-apple-quadruped-robot
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at:http://www.apache.org/licenses/LICENSE-2.0

from math import sin,cos,pi

def cal_ges(PIT,ROL,l,b,w,x,Hc):
    YA=0
    P=PIT*pi/180
    R=ROL*pi/180
    Y=YA*pi/180
    #腿1
    ABl_x=l/2 - x -(l*cos(P)*cos(Y))/2 + (b*cos(P)*sin(Y))/2
    ABl_y=w/2 - (b*(cos(R)*cos(Y) + sin(P)*sin(R)*sin(Y)))/2 - (l*(cos(R)*sin(Y) - cos(Y)*sin(P)*sin(R)))/2
    ABl_z= - Hc - (b*(cos(Y)*sin(R) - cos(R)*sin(P)*sin(Y)))/2 - (l*(sin(R)*sin(Y) + cos(R)*cos(Y)*sin(P)))/2
    #腿2
    AB2_x=l/2 - x - (l*cos(P)*cos(Y))/2 - (b*cos(P)*sin(Y))/2
    AB2_y=(b*(cos(R)*cos(Y) + sin(P)*sin(R)*sin(Y)))/2 - w/2 - (l*(cos(R)*sin(Y) - cos(Y)*sin(P)*sin(R)))/2
    AB2_z=(b*(cos(Y)*sin(R) - cos(R)*sin(P)*sin(Y)))/2 - Hc - (l*(sin(R)*sin(Y) + cos(R)*cos(Y)*sin(P)))/2
    #腿3
    AB3_x=(l*cos(P)*cos(Y))/2 - x - l/2 + (b*cos(P)*sin(Y))/2
    AB3_y=w/2 - (b*(cos(R)*cos(Y) + sin(P)*sin(R)*sin(Y)))/2 + (l*(cos(R)*sin(Y) - cos(Y)*sin(P)*sin(R)))/2
    AB3_z=(l*(sin(R)*sin(Y) + cos(R)*cos(Y)*sin(P)))/2 - (b*(cos(Y)*sin(R) - cos(R)*sin(P)*sin(Y)))/2 - Hc
    #腿4
    AB4_x=(l*cos(P)*cos(Y))/2 - x - l/2 - (b*cos(P)*sin(Y))/2
    AB4_y=(b*(cos(R)*cos(Y) + sin(P)*sin(R)*sin(Y)))/2 - w/2 + (l*(cos(R)*sin(Y) - cos(Y)*sin(P)*sin(R)))/2
    AB4_z=(b*(cos(Y)*sin(R) - cos(R)*sin(P)*sin(Y)))/2 - Hc + (l*(sin(R)*sin(Y) + cos(R)*cos(Y)*sin(P)))/2

    x1=ABl_x
    y1=ABl_z

    x2=AB2_x
    y2=AB2_z

    x3=AB4_x
    y3=AB4_z

    x4=AB3_x
    y4=AB3_z
    
    return x1,x2,x3,x4,y1,y2,y3,y4




