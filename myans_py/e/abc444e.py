from sortedcontainers import SortedList
n,d=map(int,input().split())
a=list(map(int,input().split()))

ss=SortedList()
ans,l=0,0
for r in range(n): #尺取り
    li,ri=ss.bisect_left(a[r]-d+1),ss.bisect_left(a[r]+d) #差込みの左端、右端
    while li<ri:
        ss.remove(a[l])
        l+=1
        li,ri=ss.bisect_left(a[r]-d+1),ss.bisect_left(a[r]+d)
    ss.add(a[r])
    ans+=r-l+1
print(ans)