from collections import deque

h,w=map(int, input().split())
s=list(map(int, input().split()))
c=list(map(int, input().split()))
s[0]-=1; s[1]-=1; c[0]-=1; c[1]-=1
g=[input() for i in range(h)]

d=deque()
d.append((s[0],s[1]))
cnt=[[10**18]*w for i in range(h)]
cnt[s[0]][s[1]]=-1

while d:
    i,j,=d.popleft()
    if [i,j]==c:
        break
    
    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni,nj=i+di,j+dj
        while 0<=ni<h and 0<=nj<w and g[ni][nj]=='.': # ぶつかるまで進むのが最善
            if cnt[ni][nj]<cnt[i][j]+1: break # BFSなのでover打ち切り
            
            if cnt[ni][nj]>cnt[i][j]+1:
                cnt[ni][nj]=cnt[i][j]+1
                d.append((ni,nj))
            ni+=di
            nj+=dj

print(cnt[c[0]][c[1]])