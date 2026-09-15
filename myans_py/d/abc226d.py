from math import gcd
n=int(input())
xy=[list(map(int,input().split())) for i in range(n)]
s=set()
for i in range(n):
    for j in range(n):
        if i!=j:
            x,y=xy[j][0]-xy[i][0],xy[j][1]-xy[i][1] #x,yの変化量
            g=gcd(x,y)
            s.add((x//g,y//g))
print(len(s))