from bisect import bisect_right,bisect_left
n=int(input())
a=list(map(int,input().split()))
c=[[] for i in range(2*10**5+1)]
for i in range(n):
    c[a[i]].append(i)

for _ in range(int(input())):
    l,r,x=map(int,input().split())
    l-=1; r-=1
    ans=bisect_right(c[x],r)-bisect_left(c[x],l)
    print(ans)