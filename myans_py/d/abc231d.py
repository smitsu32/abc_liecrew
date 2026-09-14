n,m=map(int,input().split())
g=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

for i in range(n):
    if len(g[i])>2: # 1->(2,3,4)はむり
        print('No')
        exit()

f=True
vst=[False]*n
for i in range(n):
    if vst[i]:
        continue
    l=[(i,-1)] #直前点も
    vst[i]=True
    while l: #サイクルないかDFS
        u,lst=l.pop()
        for v in g[u]:
            if v==lst:
                continue
            if vst[v] and v!=lst:
                f=False
                break
            vst[v]=True
            l.append((v,u))
        if not f:
            break
    if not f:
        break
print('Yes' if f else 'No')