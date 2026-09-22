n,w=map(int, input().split())
v=10**5
dp=[[10**18]*(v+1) for i in range(n+1)] #[個][価値]
dp[0][0]=0

for i in range(1,1+n):
    wi,vi=map(int, input().split())
    for j in range(v+1):
        dp[i][j]=dp[i-1][j]
        if j-vi>=0:
            dp[i][j]=min(dp[i][j],dp[i-1][j-vi]+wi)

for i in range(v,-1,-1):
    if dp[-1][i]<=w:
        print(i)
        exit()
print(0)