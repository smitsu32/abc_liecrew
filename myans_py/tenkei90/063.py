from collections import defaultdict

h,w=map(int, input().split())
p=[list(map(int, input().split())) for i in range(h)]

ans=0
for bit in range(2**h):
    used=[]
    for i in range(h):
        if bit&1<<i==0:
            used.append(i)
    if not used:
        continue
    
    d=defaultdict(int)
    for i in range(w):
        f,s=True,p[used[0]][i]
        for j in used:
            if p[j][i]!=s:
                f=False
                break
        if f:
            d[s]+=1
    if d:
        ans=max(ans,max(d.values())*len(used))
print(ans)