n=int(input())
INF=1001

# 2D-imos
cnt=[[0]*INF for i in range(INF)]
for _ in range(n):
    lx,ly,rx,ry=map(int, input().split())
    #lx-=1; ly-=1; rx-=1; ry-=1
    
    # 左上と右下を+1,残りを-1
    cnt[lx][ly]+=1
    cnt[rx][ry]+=1
    cnt[lx][ry]-=1
    cnt[rx][ly]-=1

for i in range(INF):
    for j in range(1,INF):
        cnt[i][j]+=cnt[i][j-1]
for j in range(INF):
    for i in range(1,INF):
        cnt[i][j]+=cnt[i-1][j]

ans=[0]*n
for i in range(INF):
    for j in range(INF):
        if cnt[i][j]>=1:
            ans[cnt[i][j]-1]+=1

for i in range(n):
    print(ans[i])