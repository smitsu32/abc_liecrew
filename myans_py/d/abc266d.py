n=int(input())
a=[[0]*5 for i in range(10**5+1)] #各時刻iで座標xにいたときもらえる点
for i in range(n):
    t,x,ai=map(int,input().split())
    a[t][x]+=ai

dp=[[-10**18]*5 for i in range(10**5+1)] #i秒後に座標jのとき
dp[0][0]=0
for i in range(1,1+10**5):
    for j in range(5):
        dp[i][j]=dp[i-1][j] #とどまる
        if j!=0:
            dp[i][j]=max(dp[i][j],dp[i-1][j-1]) #1マス進む
        if j!=4:
            dp[i][j]=max(dp[i][j],dp[i-1][j+1]) #1マス戻る
        dp[i][j]+=a[i][j] #そのマスの点数を加算
print(max(dp[-1]))