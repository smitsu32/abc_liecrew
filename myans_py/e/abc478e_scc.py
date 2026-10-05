from atcoder.scc import SCCGraph #強連結成分（SCC）
n,q=map(int,input().split())
scc=SCCGraph(n)

r=[] #逆順のエッジ
for _ in range(q):
    t,u,v=map(int,input().split())
    scc.add_edge(u-1,v-1)
    if t==1: r.append((u-1,v-1))

g=[0]*n #点iのトポロジカル順番号(1-indexed)
group=scc.scc() #トポロジカル順を2次元グラフ化したもの
for i in range(len(group)):
    for j in group[i]:
        g[j]=i+1

for u,v in r:
    if g[u]==g[v]: #逆順なので一緒はダメ
        print('No')
        exit()
print('Yes')
print(*g)