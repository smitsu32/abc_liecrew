n,m=map(int,input().split())
a,b=[[] for i in range(n)],[0]*n
for i in range(m):
    ai,bi=map(int,input().split())
    a[ai-1].append(bi-1)
    b[ai-1]+=1

o,t=[-1,-1],[-1,-1] #人,票数
for i in range(n):
    if o[1]<b[i]:
        t=o[:]
        o=[i,b[i]]
    elif t[1]<b[i]:
        t=[i,b[i]]

# 解説AC: 候補者iが辞退したとき上位２人と第２候補者のみ見る
for i in range(n):
    tmp=b[i] #i消去
    b[i]=0
    for j in a[i]:
        b[j]+=1
    
    ans=[-1,-1] #新1位
    for j in a[i]+[o[0]]+[t[0]]: #第２候補と1,2位
        if ans[1]<b[j] or (ans[1]==b[j] and ans[0]>j): #1位更新か、2位以下がまくってきたら
            ans=[j,b[j]]
    print(ans[0]+1)
    
    b[i]=tmp #i復元
    for j in a[i]:
        b[j]-=1