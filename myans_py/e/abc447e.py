from atcoder.dsu import DSU
n,m=map(int,input().split())
MOD=998244353

d=DSU(n+1)
u,v,cst=[0]*m,[0]*m,[0]*m
now=2
for i in range(m):
    u[i],v[i]=map(int,input().split())
    cst[i]=now
    now=(now*2)%MOD

mg=n #連結成分数
ans=0
for i in range(m-1,-1,-1):
    if not d.same(u[i],v[i]):
        if mg>2:
            d.merge(u[i],v[i])
            mg-=1
        else: #連結数2ならもうだめ
            ans=(ans+cst[i])%MOD
print(ans)