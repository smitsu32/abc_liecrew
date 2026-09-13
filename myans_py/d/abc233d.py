from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
s=[0]
for i in range(n):
    s.append(s[-1]+a[i])

ans=0
d=defaultdict(int)
d[0]+=1
for i in range(1,n+1): #右端で探索
    ans+=d[s[i]-k] # s[l]=s[r]-k
    d[s[i]]+=1 #右端を追加
print(ans)