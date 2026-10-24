from heapq import heappop,heappush
n,m,s,t=map(int,input().split())
g=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

mn=[0]*n
for i in range(n):
    if len(g[i])>0:
        mn[i]=min(g[i])

dis=[10**18]*n
dis[s-1]=0
h=[(0,s-1)] #重み付きだからcostが先
while h:
    cst,u=heappop(h)
    if cst>dis[u]: continue
    for v in g[u]:
        if mn[u]==v and cst<dis[v]:
            dis[v]=cst
            heappush(h,(cst,v))
        elif mn[u]!=v and cst+1<dis[v]:
            dis[v]=cst+1
            heappush(h,(cst+1,v))

if dis[t-1]!=10**18:
    print(dis[t-1])
else:
    print(-1)