from bisect import bisect_right
n,q=map(int,input().split())
r=sorted(list(map(int,input().split())))
s=[0]
for i in range(n):
    s.append(s[-1]+r[i])

for _ in range(q):
    x=int(input())
    print(bisect_right(s,x)-1)