from collections import deque
a,n=map(int,input().split())
m=10**len(str(n)) #max

cnt=[-1]*m
cnt[1]=0
d=deque([1])
while d:
    i=d.popleft()
    if i==n: break
    if i*a<=m and cnt[i*a]==-1:
        d.append(i*a)
        cnt[i*a]=cnt[i]+1
    if i>=10 and i%10!=0:
        si=str(i)
        ii=int(si[-1]+si[:-1])
        if ii<=m and cnt[ii]==-1:
            d.append(ii)
            cnt[ii]=cnt[i]+1
print(cnt[n])