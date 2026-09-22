from math import sin,cos,pi,atan2

t=int(input())
l,x,y=map(int,input().split())

for _ in range(int(input())):
    e=int(input())
    # 観覧車の現在の角度→座標を出す
    rad=e/t*2*pi
    ynow,znow=-l/2*sin(rad),-l/2*cos(rad)+l/2
    # 仰角
    ans=atan2(znow,(x**2+(y-ynow)**2)**0.5)
    print(ans*180/pi)