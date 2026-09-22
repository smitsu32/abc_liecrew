import sys
sys.setrecursionlimit(10**6)

n=int(input())

g=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1; b-=1
    g[a].append(b)
    g[b].append(a)

# 0,1で隣を色分け
used=[-1]*n
def dfs(s,pal):
    used[s]=pal
    for v in g[s]:
        if used[v]==-1:
            dfs(v,1-pal)
dfs(0,0)

ans1,ans2=[],[]
for i in range(n):
    if used[i]==0:
        ans1.append(i+1)
    else:
        ans2.append(i+1)

# 多い方のn/2個を取り出し
if len(ans1)>=len(ans2):
    print(*ans1[:n//2])
else:
    print(*ans2[:n//2])