n,q=map(int,input().split())

f,c=set(),['a']*n #タイル有無、色
cnt=[0]*n #クエリ2の回数
now=0 # 上が今何回か
ac='a' #今のタイルなしの色
for _ in range(q):
    qu=input().split()
    if qu[0]=='1':
        x=int(qu[1])-1
        if x in f: #タイルあり
            f.remove(x)
            cnt[x]=now
        else:
            f.add(x)
            if cnt[x]<now: #全体更新があったら更新
                c[x]=ac
    else:
        ac=qu[1]
        now+=1

ans=[]
for i in range(n):
    if i in f or cnt[i]==now: #タイルありか全体更新関係なし
        ans.append(c[i])
    else:
        ans.append(ac)
print(''.join(ans))