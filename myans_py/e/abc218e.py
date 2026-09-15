from atcoder.dsu import DSU
n,m=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(m)]
abc.sort(key=lambda x:x[2])

uf=DSU(n+1) #最小全域木(クラスカル法)
ans=sum(abc[i][2] for i in range(m)) #重み
for a,b,c in abc:
    if not uf.same(a,b) or c<0: #最小じゃなくていい（負は残せる）
        uf.merge(a,b)
        ans-=c #ない状態(全受取)から報酬の少ない点をなかったことにする
print(ans)