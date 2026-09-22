k=int(input())
MOD=10**9+7

if k%9!=0:
    print(0)
else:
    # dp[i]:各桁の和がiになる数の総数
    dp=[0]*(k+1)
    dp[0]=1
    # ゴール段でfor
    for i in range(1,k+1):
        for j in range(1,10):
            if j>i: break # 9段までしか昇れない
            dp[i]=(dp[i]+dp[i-j])%MOD # 1~9段下から昇る階段みたいな
    print(dp[-1])