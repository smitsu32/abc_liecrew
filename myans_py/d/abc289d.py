n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
x=int(input())

dp=[True]+[False]*x
for i in range(x):
    if not dp[i]: continue
    for j in range(n):
            if i+a[j] not in b and i+a[j]<=x:
                dp[i+a[j]]=True
print('Yes' if dp[-1] else 'No')