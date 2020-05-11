clc;
clear;
Ts=1; %周期
fai=0.5; %支撑相占空比
xs=-10;  %起点x位置
xf=40; %终点x位置
zs=0;  %z起点位置
h=30;  %抬腿高度

x=[]; %设定数组用于保存x坐标值
z=[]; %设定数组用于保存z坐标值


for t=0:0.01:Ts*fai        %for循环，从0开始到0.5,间隔0.01循环赋值给t,制造出时刻数值
    sigma=2*pi*t/(fai*Ts); %计算sigma值
    xep=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs; %根据时刻计算x轴离散点
    zep=h*(1-cos(sigma))/2+zs;                  %根据时刻计算z轴离散点
    x=[x,xep];                               %放在x数组里，准备画图
    z=[z,zep];                               %放在z数组里，准备画图
end
plot(x,z)                                    %指定两个数组，分别画图