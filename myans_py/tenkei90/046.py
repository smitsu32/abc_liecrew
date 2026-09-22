from collections import defaultdict

n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
MOD=46

da,db,dc=defaultdict(int),defaultdict(int),defaultdict(int)
for i in range(n):
    da[a[i]%MOD]+=1
    db[b[i]%MOD]+=1
    dc[c[i]%MOD]+=1

ans=0
# O(46**3)<O(10**6)
for i in range(MOD):
    for j in range(MOD):
        for k in range(MOD):
            if (i+j+k)%MOD==0:
                ans+=da[i]*db[j]*dc[k]

print(ans)