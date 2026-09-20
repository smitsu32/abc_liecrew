from atcoder.segtree import SegTree
n,m=map(int,input().split())
p=list(map(int,input().split()))
INF=10**18

def op_min(a,b): #小さい方を返す演算条件 (関数)
    return a if a[0]<b[0] else b
def op_max(a,b):
    return a if a[0]>b[0] else b
e_min,e_max=(INF,-1),(-INF,-1) #単位元(min,max、固定で使える)

#(演算op、単位元e、要素とindexのセット(min,maxだけでなく順番も取り出したいから))
seg_min=SegTree(op_min,e_min,[(p[i],i) for i in range(n)])
seg_max=SegTree(op_max,e_max,[(p[i],i) for i in range(n)])

for _ in range(m):
    l,r=map(int,input().split())
    l-=1
    vmn,imn=seg_min.prod(l,r) #[l,r)の最小値,そのindex
    vmx,imx=seg_max.prod(l,r)
    
    p[imn],p[imx]=p[imx],p[imn] #入れ替え
    
    seg_min.set(imn,(p[imn],imn)) #それぞれのセグ木の中身も更新
    seg_min.set(imx,(p[imx],imx))
    seg_max.set(imn,(p[imn],imn))
    seg_max.set(imx,(p[imx],imx))

print(*p)