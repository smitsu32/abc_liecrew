n=int(input())
a=list(map(int,input().split()))

INF=2*10**5+1
cnt=[0]*INF #整数iの数（累積和）
for i in range(n):
    cnt[a[i]]+=1
for i in range(1,INF):
    cnt[i]+=cnt[i-1]

ans=0
for i in range(1,INF): #真ん中
    ans+=(cnt[i]-cnt[i-1])*cnt[i-1]*(n-cnt[i]) #真ん中*前*後(i+1~最後)
print(ans)