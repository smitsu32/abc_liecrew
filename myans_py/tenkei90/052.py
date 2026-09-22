n=int(input())
a=[list(map(int, input().split())) for i in range(n)]
MOD=10**9+7

# 各さいころ目の和
s=[0]*n
for i in range(n):
    s[i]=sum(a[i])

# 因数分解するとすべての面の積
ans=1
for i in range(n):
    ans*=s[i]

print(ans%MOD)