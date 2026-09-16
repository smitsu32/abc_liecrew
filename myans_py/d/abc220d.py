n=int(input())
a=list(map(int,input().split()))
MOD=998244353
dp=[[0]*10 for i in range(n+1)] #Aiまで終了時の先頭jが何通りか
dp[1][a[0]]=1
for i in range(1,n):
    for j in range(10):
        dp[i+1][(j+a[i])%10]+=dp[i][j]
        dp[i+1][(j*a[i])%10]+=dp[i][j]
        dp[i+1][(j+a[i])%10]%=MOD
        dp[i+1][(j*a[i])%10]%=MOD

for i in range(10):
    print(dp[-1][i]%MOD)