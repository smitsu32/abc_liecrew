n=int(input())
p=list(map(float, input().split()))

dp=[[0]*(n+1) for i in range(n+1)] #iで表j
dp[0][0]=1
for i in range(1,n+1):
    for j in range(i+1):
        if j>0: # 表j回+裏　と　表j-1回+表
            dp[i][j]=dp[i-1][j]*(1-p[i-1])+dp[i-1][j-1]*p[i-1]
        else: #まだ表がないとき
            dp[i][j]=dp[i-1][j]*(1-p[i-1])

ans=0
for i in range(n//2+1,n+1):
    ans+=dp[-1][i]
print(ans)