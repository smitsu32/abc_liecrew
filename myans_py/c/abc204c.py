n,m=map(int,input().split())
g=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

ans=0
for i in range(n):
    l,vst=[i],[False]*n
    vst[i]=True
    ans+=1
    while l:
        u=l.pop()
        for v in g[u]:
            if not vst[v]:
                l.append(v)
                vst[v]=True
                ans+=1
print(ans)