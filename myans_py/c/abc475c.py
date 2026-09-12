n,s,l=map(int,input().split())
s-=1
a=list(map(int,input().split()))
c=[0]
for i in range(n-1):
    c.append(c[-1]+a[i])

ans=1
for le in range(s+1):
    dl=c[s]-c[le]
    if dl>l:
        continue
    for r in range(s,n):
        dr=c[r]-c[s]
        if min(dl*2+dr,dl+dr*2)<=l:
            ans=max(ans,r-le+1)
print(ans)