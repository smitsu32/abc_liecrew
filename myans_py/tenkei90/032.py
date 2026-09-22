from itertools import permutations

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

dis=set()
m=int(input())
for i in range(m):
    u,v=map(int,input().split())
    dis.add((u,v))
    dis.add((v,u))

ans=10**18
for l in list(permutations(range(1,n+1))):
    tmp=0
    ok=True
    for i in range(n-1):
        if (l[i],l[i+1]) in dis:
            ok=False
            break
        tmp+=a[l[i]-1][i]
    if ok:
        tmp+=a[l[-1]-1][-1]
        ans=min(ans,tmp)

if ans!=10**18:
    print(ans)
else:
    print(-1)