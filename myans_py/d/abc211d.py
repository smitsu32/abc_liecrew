from collections import deque
n,m=map(int,input().split())
MOD=10**9+7
g=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

cnt=[0]*n #答え
dis=[-1]*n #0からの距離
cnt[0],dis[0]=1,0
d=deque([0])
while d:
    u=d.popleft()
    for v in g[u]:
        if dis[v]==-1: #未到達
            dis[v]=dis[u]+1
            cnt[v]=cnt[u]
            d.append(v)
        elif dis[v]==dis[u]+1: #同じ短さなら足すだけ
            cnt[v]=(cnt[v]+cnt[u])%MOD
            # d.append(v) # ifで済んでる
print(cnt[-1]%MOD)