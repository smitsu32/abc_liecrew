n,k=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]

INF=10**18
m=2*k+1 #最大区間数(裏がk区間より)
dp=[[-INF]*(m+1) for _ in range(n+1)] #i枚目まで区間j個の最大値
dp[0][0]=dp[0][1]=0

for i in range(n):
    for j in range(m):
        if j%2==0:
            # jで区間分けるor区間継続　+　表の値
            dp[i+1][j+1]=max(dp[i][j],dp[i][j+1])+ab[i][0]
        else:
            dp[i+1][j+1]=max(dp[i][j],dp[i][j+1])+ab[i][1]
print(max(dp[-1]))