import math
n=int(input())
a=list(map(int,input().split()))
g=0
for i in range(n):
    g=math.gcd(g,a[i]) #gcd(0,a)=a

ans=0
for i in range(n):
    a[i]//=g
    while a[i]%2==0:
        a[i]//=2
        ans+=1
    while a[i]%3==0:
        a[i]//=3
        ans+=1
    if a[i]!=1:
        print(-1)
        exit()
print(ans)