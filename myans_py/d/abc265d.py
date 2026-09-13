n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
s=[0]
for i in range(n):
    s.append(s[-1]+a[i])
s=set(s)

for i in s:
    if i+p in s and i+p+q in s and i+p+q+r in s: #sy=sx+p,sz=sx+p+q,sw=sx+p+q+r
        print('Yes')
        exit()
print('No')