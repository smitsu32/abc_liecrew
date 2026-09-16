n=int(input())
t=list(map(int,input().split()))
st=sum(t)

dp=[[False]*(st+1) for i in range(n+1)] #料理0~iで時刻jに到達可能か
dp[0][0]=True
for i in range(n):
    for j in range(st+1):
        if dp[i][j]:
            dp[i+1][j]=True
            dp[i+1][j+t[i]]=True

ans=10**18
for i in range(st+1):
    if dp[n][i]:
        ans=min(ans,max(i,st-i)) #最短調理可能時間
print(ans)