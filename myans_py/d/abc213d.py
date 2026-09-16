import sys; sys.setrecursionlimit(10**6)
n=int(input())
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1); g[b-1].append(a-1)
g=[sorted(i) for i in g]

def f(u,lst): #DFS
    ans.append(u+1)
    for v in g[u]:
        if v!=lst:
            f(v,u)
            ans.append(u+1) #戻ってきたら今の点を記録

ans=[]
f(0,-1)
print(*ans)