from atcoder.dsu import DSU
n=int(input())
a=list(map(int,input().split()))

d=DSU(2*10**5+1)
for i in range(n//2):
    d.merge(a[i],a[n-1-i])

s2=set()
for i in a:
    s2.add(d.leader(i)) #登場する点のみ連結数をとる
# 点種類数 - 連結成分数
# A=1233なら1=3,2=3にならないといけないので結局1=2=3 (点種類3-1種類=2個減らす)
print(len(set(a))-len(s2))