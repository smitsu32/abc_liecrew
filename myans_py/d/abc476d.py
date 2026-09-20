from bisect import bisect_left,bisect_right
n,m,k=map(int,input().split())
x,y=map(int,input().split())
a,b=sorted(list(map(int,input().split()))),sorted(list(map(int,input().split())))
na=[0]
for i in range(n):
    na.append(na[-1]+a[i])

nx,ny=x,y
ans=0
for i in range(-1,m): #bから選ぶ個数(0-indexed)
    if i!=-1:
        ny-=(b[i]+k-1)//k #kドル減少分
        nx+=(-b[i])%k #1ドル増加分(あまり)
    if ny<0: break
    ans=max(ans,(i+1)+bisect_right(na,ny*k+nx)-1) #aの個数+bの個数
print(ans)