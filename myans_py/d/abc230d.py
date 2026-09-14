n,d=map(int,input().split())
lr=[list(map(int,input().split())) for i in range(n)]
lr.sort(key=lambda x:x[1])

ans=0
x=-10**18
for l,r in lr: #区間スケジューリング問題
    if x+d<=l: #区間外(最大rがlより左)なら足す
        ans+=1
        x=r
print(ans)