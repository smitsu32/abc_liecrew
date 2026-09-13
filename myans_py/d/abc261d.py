from collections import defaultdict
n,m=map(int,input().split())
x=list(map(int,input().split()))
y=defaultdict(int)
for i in range(m):
    c,yi=map(int,input().split())
    y[c]=yi

dp=[[-10**18]*(n+1) for i in range(n+1)] #i回目にカウンタj
dp[0][0]=0
for i in range(1,n+1):
    for j in range(n+1):
        if j!=0:
            dp[i][j]=dp[i-1][j-1]+x[i-1]+y[j] #そのときのX+Y
        else:
            dp[i][j]=max(dp[i-1]) #0のとき戻す
print(max(dp[-1]))