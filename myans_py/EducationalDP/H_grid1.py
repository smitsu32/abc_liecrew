h,w=map(int, input().split())
a=[input() for i in range(h)]
MOD=10**9+7

dp=[[0]*(w+1) for i in range(h+1)]
dp[1][1]=1
for i in range(1,1+h): # 0は番兵
    for j in range(1,1+w):
        if a[i-1][j-1]=='#':
            dp[i][j]=0
        else:
            dp[i][j]=max(dp[i][j],dp[i-1][j]+dp[i][j-1])%MOD

print(dp[-1][-1]%MOD)