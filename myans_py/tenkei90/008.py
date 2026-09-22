n=int(input())
s=input()
MOD=10**9+7

#DP
dp=[[0]*8 for _ in range(n+1)]
dp[0][0]=1
al='atcoder'

for i in range(n):
    for j in range(8):
        dp[i+1][j]+=dp[i][j] # 1つ前のループの結果をたす(s[i]を使わない場合, 完成済の場合)
        if j<7 and s[i]==al[j]:
            dp[i+1][j+1]+=dp[i][j] # 各文字について1個前のalまでの通り数ぶんたす(s[i]を使う場合)

print(dp[-1][-1]%MOD)