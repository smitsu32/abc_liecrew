#AI解
from atcoder.dsu import DSU
n=2**20
a=[-1]*n
uf=DSU(n) #根
nxt=[i for i in range(n)] #次の空き場所

for _ in range(int(input())):
    t,x=map(int,input().split())
    if t==1: # !=1のパスの連続がネック→参照先をUnionFindで経路圧縮
        i=nxt[uf.leader(x%n)]
        a[i]=x
        ni=nxt[uf.leader((i+1)%n)] #次の空き点
        r=uf.merge(i,(i+1)%n) #r:根
        nxt[r]=ni
    else:
        print(a[x%n])