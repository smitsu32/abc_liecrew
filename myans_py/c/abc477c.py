q=int(input())
s,t=input(),input()
n,m=len(s),len(t)
ok=[0]*(n+1) #1-indexed
for i in range(n-m+1):
    ok[i+1]=ok[i]
    if s[i:i+m]==t:
        ok[i+1]+=1

for _ in range(q):
    l,r=map(int,input().split())
    l-=1; r-=m
    if r>=l and ok[r+1]-ok[l]>0:
        print('Yes')
    else:
        print('No')