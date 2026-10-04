n,k=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(a)

l=[]
for i in range(n):
    if a[i]!=b[i]:
        l.append(i) #差分が違うとこだけindexを格納

if not l or l[-1]-l[0]+1<=k:
    print('Yes')
else:
    print('No')