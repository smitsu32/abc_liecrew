n=int(input())
sx,sy,tx,ty=map(int,input().split())
xyr=[list(map(int,input().split())) for i in range(n)]
g=[[] for i in range(n)]
st,gl=-1,-1
for i in range(n):
    xi,yi,ri=xyr[i]
    if (xi-sx)**2+(yi-sy)**2==ri**2: st=i
    if (xi-tx)**2+(yi-ty)**2==ri**2: gl=i    
    for j in range(i+1,n):
        xj,yj,rj=xyr[j]
        if (ri-rj)**2<=(xi-xj)**2+(yi-yj)**2<=(ri+rj)**2:
            g[i].append(j)
            g[j].append(i)
if st==-1 or gl==-1:
    print('No')
    exit()

l=[st]
vst=[False]*n
vst[st]=True
while l:
    u=l.pop()
    for v in g[u]:
        if not vst[v]:
            vst[v]=True
            l.append(v)
print('Yes' if vst[gl] else 'No')