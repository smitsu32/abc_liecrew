n,q=map(int,input().split())

a,d=[[] for _ in range(n+1)],[[] for _ in range(n+1)] #追加、削除される数
for _ in range(q):
    l,r,x=map(int,input().split())
    a[l-1].append(x)
    d[r].append(x)

cnt=[0]*(q+1) #値xが何個の区間がおおってるか
ans=[]
c=0
for i in range(n): #位置で走査(クエリではない)
    for j in d[i]: #イベントソート:削除が先
        cnt[j]-=1
        if cnt[j]==0: c-=1
    for j in a[i]:
        cnt[j]+=1
        if cnt[j]==1: c+=1
    ans.append(c)
print(*ans)