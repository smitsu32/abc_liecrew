n,k=map(int, input().split())
MOD=10**5

if n==0:
    exit(print(0))

l=[n]
d=[[] for _ in range(MOD+1)]
d[n].append(0)

for j in range(1,1+MOD):
    i=l[-1]
    ni=i
    while ni>0:
        i+=ni%10
        ni//=10
    i%=MOD
    l.append(i)
    d[i].append(j)
    if len(d[i])>1:
        a=d[i]
        break

if k<=a[0]:
    print(l[k])
else:
    print(l[(k-a[0])%(a[1]-a[0])+a[0]])