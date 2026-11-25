n=int(input())
s=input()

#解説AC:真ん中の取りうる最大範囲で尺取り法
l,r,f=-1,n-1,[False]*3
for i in range(n):
    f[ord(s[i])-65]=True
    if f==[True]*3:
        l=i+1
        break
f=[False]*3
for i in range(n-1,-1,-1):
    f[ord(s[i])-65]=True
    if f==[True]*3:
        r=i
        break

if l<0 or l+3>r:
    print(0)
    exit()

ans,rr=0,l
cnt=[0]*3 #ABC
for ll in range(l,r):
    while rr<r and min(cnt)==0:
        cnt[ord(s[rr])-65]+=1
        rr+=1
    if min(cnt)==0: #もう作れなければbreak
        break
    ans+=r-rr+1 #右端のマージン
    cnt[ord(s[ll])-65]-=1
print(ans)