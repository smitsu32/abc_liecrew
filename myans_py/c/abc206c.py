from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))

d=defaultdict(int)
for i in range(n):
    d[a[i]]+=1

ans=0
for k,v in d.items():
    ans+=v*(n-v)
print(ans//2)