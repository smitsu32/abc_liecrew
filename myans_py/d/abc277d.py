from atcoder.dsu import DSU
from collections import defaultdict
n,m=map(int, input().split())
a=list(map(int, input().split()))
d,idx=defaultdict(int),defaultdict(int) #idx:union-findで繋げる仮想index
j=1
for i in range(n):
    d[a[i]]+=a[i]
    if idx[a[i]]==0:
        idx[a[i]]=j
        j+=1

ds=DSU(j) #UFで接続→連鎖捨て
for k,v in list(idx.items()): #k:カード値、v:idx
    x=(k+1)%m
    if idx[x]!=0:
        ds.merge(v,idx[x])
ans=[0]*j #各カードから始めたときの捨てる最大値
for k,v in list(idx.items()):
    ans[ds.leader(v)]+=d[k]
print(sum(a)-max(ans))