n=int(input())
x=list(map(int,input().split()))

if n==1: exit(print(0))

for i in range(n):
    if i==0 or i==n-1:
        ans=(x[-1]-x[0])//2
    else:
        # xが左かつx-1が右
        ans1=max((x[i]-x[0])//2,(x[-1]-x[i-1])//2)
        # xが右かつx+1が左
        ans2=max((x[-1]-x[i])//2,(x[i+1]-x[0])//2)
        ans=min(ans1,ans2)
    print(ans)