# Time: 5sec
from itertools import combinations

n,p,q=map(int, input().split())
a=list(map(int, input().split()))

ans=0
for l in combinations(a,5):
    cur=1
    for i in l:
        cur=cur*i%p
    if cur%p==q:
        ans+=1

print(ans)