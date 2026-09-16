from collections import deque
d=deque()
for _ in range(int(input())):
    q,*a=map(int,input().split())
    if q==1:
        d.append(tuple(a)) #x,c
    else:
        ans,cnt,n=0,0,a[0]
        while cnt<n:
            x,c=d.popleft()
            if cnt+c>n:
                d.appendleft((x,c-(n-cnt)))
                ans+=x*(n-cnt)
                cnt=n
            else:
                cnt+=c
                ans+=x*c
        print(ans)