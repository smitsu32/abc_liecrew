n,w=map(int, input().split())
dp=[[0]*(1+w) for i in range(n+1)]

for i in range(1,1+n):
    wi,vi=map(int, input().split())
    for j in range(w+1):
        dp[i][j]=dp[i-1][j]
        if j-wi>=0:
            dp[i][j]=max(dp[i][j],dp[i-1][j-wi]+vi)

print(dp[-1][-1])