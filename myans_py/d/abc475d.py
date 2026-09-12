from itertools import permutations
s=list(input())
n=len(s)
p=[True]*10**n
p[0],p[1]=False,False
for i in range(2,int((10**n)**0.5)+1):
    if p[i]:
        for j in range(i*i,10**n,i):
            p[j]=False

t=list(set(s))
m=len(t)
for l in list(permutations(range(10),m)):
    d=dict()
    for i in range(m):
        d[t[i]]=l[i]
    ss=[0]*n
    for i in range(n):
        ss[i]=d[s[i]]
    if ss[0]==0:
        continue
    sss=0
    for i in range(n):
        sss=sss*10+ss[i]
    
    if p[sss]:
        print(sss)
        exit()
print(-1)