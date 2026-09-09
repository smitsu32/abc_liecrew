from collections import defaultdict

n=int(input())
d=defaultdict(lambda:len(d)) #追加の都度indexを更新
g=[[] for i in range(2*n)]
sta=[True]*(2*n) #始点か
for i in range(n):
    s,t=input().split()
    g[d[s]].append(d[t])
    sta[d[t]]=False

f=True
vst=[False]*(2*n)
for i in range(2*n):
    if sta[i]:
        l=[i]
        vst[i]=True
        while l:
            u=l.pop()
            for v in g[u]:
                if vst[v]:
                    f=False #ループ
                vst[v]=True
                l.append(v)

for i in range(2*n): #全サイクル
    if not vst[i]:
        f=False
        break
print('Yes' if f else 'No')