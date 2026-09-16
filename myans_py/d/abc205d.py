from bisect import bisect_left
n,q=map(int,input().split())
a=[0]+list(map(int,input().split())) #1-indexed
b=[a[i]-i for i in range(n+1)] #aiまでに抜けている数
for _ in range(q):
    k=int(input())
    j=bisect_left(b,k)
    print(k+j-1) #[0]をひく