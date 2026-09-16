n,m,d=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort(); b.sort(); a,b=a[::-1],b[::-1]

i,j=0,0
while i<n and j<m:
    if abs(a[i]-b[j])<=d:
        print(a[i]+b[j])
        exit()
    if a[i]<b[j]:
        j+=1
    else:
        i+=1
print(-1)