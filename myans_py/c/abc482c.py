from bisect import bisect_left,bisect_right
h,w,n,q=map(int,input().split())
R,C=[],[]
for i in range(n):
    ri,ci=map(int,input().split())
    R.append(ri); C.append(ci)
R.sort(); C.sort()

for _ in range(q):
    L=list(map(int,input().split()))
    l,r=L[1:]
    if L[0]==1:
        print(bisect_right(R,r)-bisect_left(R,l))
    else:
        print(bisect_right(C,r)-bisect_left(C,l))