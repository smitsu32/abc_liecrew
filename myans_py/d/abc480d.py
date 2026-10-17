from bisect import bisect_left,bisect_right
n,q=map(int,input().split())
a=list(map(int,input().split()))

s=[0]
for i in range(n):
    s.append(s[-1]+a[i])
ss=[0] #等差数列ごとの累積和
for i in range(n):
    ss.append(ss[-1]+s[i+1])
ln=[0] #ss[i]の長さ
for i in range(n):
    ln.append(ln[-1]+i+1)

for _ in range(q):
    l,r=map(int,input().split())
    #r,lが入るブロックを探す
    br,bl=bisect_right(ln,r)-1,bisect_right(ln,l-1)-1 #累積和は1-indexed
    ansr,ansl=ss[br]+s[r-ln[br]],ss[bl]+s[l-1-ln[bl]]
    print(ansr-ansl)