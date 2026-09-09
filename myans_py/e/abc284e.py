import sys
sys.setrecursionlimit(10**6)

n,m=map(int, input().split())
g=[[] for i in range(n)]
for i in range(m):
    u,v=map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

vst=[False]*n
l=[]
ans=0
def dfs(u):
    global ans
    if ans>=10**6:
        return
    vst[u]=True
    l.append(u)
    ans+=1
    for v in g[u]:
        if not vst[v]:
            dfs(v)
    vst[u]=False
    l.pop()

dfs(0)
print(ans)