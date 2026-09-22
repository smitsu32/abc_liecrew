from collections import defaultdict

n,k=map(int, input().split())
a=list(map(int, input().split()))

cnt=0
d=defaultdict(int)
ans=0

j=0
# 右端
for i in range(n):
    if d[a[i]]==0:
        cnt+=1
    d[a[i]]+=1
    
    # (種類数)<=Kまで左端を更新
    while cnt>k:
        d[a[j]]-=1
        if d[a[j]]==0:
            cnt-=1
        j+=1
    
    ans=max(ans,i-j+1)

print(ans)