n,w=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]

ans=0
for bit in range(2**n):
    used=[False]*n
    for i in range(n):
        if bit>>i&1:
            used[i]=True
    
    d,s=0,0
    for i in range(n):
        if used[i]:
            d+=ab[i][0]
            s+=ab[i][1]
    if s<=w:
        ans=max(ans,d)
print(ans)