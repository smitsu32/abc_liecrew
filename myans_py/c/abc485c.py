n=int(input())
c=list(map(int,input().split()))
# 解説AC:左右から探索
l,r=[-1]*n,[-1]*n
for i in range(1,n):
    if c[i]==c[i-1]:
        l[i]=l[i-1]
    else:
        l[i]=i-1
for i in range(n-1,0,-1):
    if c[i]==c[i-1]:
        r[i-1]=r[i]
    else:
        r[i-1]=i

ans=[10**18]*n
for i in range(n):
    if l[i]>=0:
        ans[i]=min(ans[i],abs(l[i]-i))
    if r[i]>=0:
        ans[i]=min(ans[i],abs(r[i]-i))
print(*ans)