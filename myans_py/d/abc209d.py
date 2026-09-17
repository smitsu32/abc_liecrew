n,q=map(int,input().split())
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    
f=[-1]*n #2色に分ける(同色スタートで街)
d,f[0]=[0],0
while d:
    u=d.pop()
    for v in g[u]:
        if f[v]==-1:
            f[v]^=f[u]
            d.append(v)

for _ in range(q):
    c,d=map(int,input().split())
    print('Town' if f[c-1]==f[d-1] else 'Road')