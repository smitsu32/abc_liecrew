from collections import deque
n,q=map(int,input().split())
h,t=[-1]*n,[-1]*n #前,後ろのindex
for _ in range(q):
    qu=list(map(int,input().split()))
    if qu[0]==1:
        x,y=qu[1:]
        h[y-1],t[x-1]=x-1,y-1
    elif qu[0]==2:
        x,y=qu[1:]
        h[y-1],t[x-1]=-1,-1
    else:
        x,ans=qu[1]-1,deque([qu[1]])
        while True:
            if h[x]==-1:
                break
            ans.appendleft(h[x]+1)
            x=h[x]
        x=qu[1]-1
        while True:
                    if t[x]==-1:
                        break
                    ans.append(t[x]+1)
                    x=t[x]
        print(len(ans),*ans)