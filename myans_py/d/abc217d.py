# https://qiita.com/tatyam/items/492c70ac4c955c055602
from sortedcontainers import SortedSet
l,q=map(int,input().split())
s=SortedSet()
s.add(0); s.add(l)
for _ in range(q):
    c,x=map(int,input().split())
    if c==1:
        s.add(x)
    else:
        i=s.bisect_left(x)
        print(s[i]-s[i-1]) #真に小さいのはs[i-1]