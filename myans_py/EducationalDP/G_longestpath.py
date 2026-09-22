import sys
sys.setrecursionlimit(10**6)
from functools import cache

@cache
# トポロジカルソート(有向グラフを並べる)
def f(x):
    global flag,dp
    if flag[x]:
        return dp[x]
    
    flag[x]=True
    fans=0
    for i in g[x]:
        fans=max(fans,f(i)+1)
    dp[x]=fans
    return fans

n,m=map(int, input().split())
g=[[] for i in range(n)]
for i in range(m):
    x,y=map(int, input().split())
    g[x-1].append(y-1)

flag=[False]*n
dp=[-1]*n
ans=0
for i in range(n):
    ans=max(ans,f(i))

print(ans)