n=int(input())
a=list(map(int,input().split()))

#解説AC: kより右側が全て-2Ak -> 左右からの最大・最小値で累積和
s=[0]
for i in range(n):
    s.append(s[-1]+a[i])

lmin,lmax,rmin,rmax=[0]*(n+1),[0]*(n+1),[s[-1]]*(n+1),[s[-1]]*(n+1)
for i in range(n): #1-indexed
    lmin[i+1]=min(lmin[i],s[i+1])
    lmax[i+1]=max(lmax[i],s[i+1])
for i in range(n,0,-1): #0-indexed
    rmin[i-1]=min(rmin[i],s[i-1])
    rmax[i-1]=max(rmax[i],s[i-1])

ans=lmax[-1]-lmin[-1]+1
for i in range(n): #反転位置
    ai=max(lmax[i],rmax[i+1]-2*a[i])-min(lmin[i],rmin[i+1]-2*a[i])+1 # l | r+1
    ans=max(ans,ai)
print(ans)