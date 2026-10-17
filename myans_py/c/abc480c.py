n,k,t=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

r,ans=0,0
for i in range(n):
    if a[i]>t: break
    if a[i]>r:
        ans+=(a[i]-1-r)//k+1
    r=max(r,a[i]+k)
ans+=max(0,(t-1-r)//k+1)
print(ans)