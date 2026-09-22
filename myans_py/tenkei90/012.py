from atcoder.dsu import DSU

h,w=map(int,input().split())
vec=[[1,0],[-1,0],[0,1],[0,-1]]
red=[False]*(h*w+1)

# UnionFind 0-indexedで
d=DSU(h*w+1)
for _ in range(int(input())):
    q=list(map(int,input().split()))
    if q[0]==1:
        r,c=q[1],q[2]
        r-=1;c-=1
        red[r*w+c]=True
        for dr,dc in vec:
            nr,nc=r+dr,c+dc
            if 0<=nr<h and 0<=nc<w and red[nr*w+nc]:
                d.merge(nr*w+nc,r*w+c)
    else:
        ra,ca,rb,cb=q[1],q[2],q[3],q[4]
        ra-=1; ca-=1; rb-=1; cb-=1
        if red[ra*w+ca] and red[rb*w+cb] and d.same(ra*w+ca,rb*w+cb):
            print('Yes')
        else:
            print('No')