n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[[-10**18]*(m+1) for i in range(n+1)] #Aiでj番目まで使用しているとき
dp[0][0]=0
for i in range(1,n+1):
    for j in range(m+1):
        if j==0:
            dp[i][j]=0
        else:
            if i>=j: #選ぶ数の個数は追い越さない
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+a[i-1]*j)
print(dp[-1][-1])