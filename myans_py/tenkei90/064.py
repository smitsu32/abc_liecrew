n,q=map(int, input().split())
a=list(map(int, input().split()))
b=[a[i+1]-a[i] for i in range(n-1)] #階差

ans=sum(abs(b[i]) for i in range(n-1))
for i in range(q):
    l,r,v=map(int, input().split())
    l-=1; r-=1
    if l>=1:
        ans-=abs(b[l-1])
        b[l-1]+=v
        ans+=abs(b[l-1])
    if r<n-1:
        ans-=abs(b[r])
        b[r]-=v
        ans+=abs(b[r])
    print(ans)