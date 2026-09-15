from bisect import bisect_left,bisect_right
n=int(input())
xy=set()
for i in range(n):
    xi,yi=map(int,input().split())
    xy.add((xi,yi))

ans=0
for xi,yi in xy:
    for xj,yj in xy:
        if xi<xj and yi<yj and (xi,yj) in xy and (xj,yi) in xy:
            ans+=1
print(ans)