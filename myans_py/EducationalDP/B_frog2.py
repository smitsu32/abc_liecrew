n,k=map(int, input().split())
h=list(map(int, input().split()))

dp=[10**18]*n
dp[0]=0
for i in range(n):
    for j in range(1,1+k):
        if i+j<n:
            dp[i+j]=min(dp[i+j],dp[i]+abs(h[i]-h[i+j]))

print(dp[-1])