from collections import deque
n,m=map(int,input().split())
vec=[]
for i in range(n):
    for j in range(n):
        if i**2+j**2==m:
            for di,dj in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                vec.append((i*di,j*dj))

g=[[-1]*n for i in range(n)]
g[0][0]=0
d=deque([(0,0)])
while d: #bfs
    i,j=d.popleft()
    for di,dj in vec:
        ni,nj=i+di,j+dj
        if 0<=ni<n and 0<=nj<n and g[ni][nj]==-1:
            g[ni][nj]=g[i][j]+1
            d.append((ni,nj))
for l in g:
    print(*l)