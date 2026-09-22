n,k=map(int, input().split())
m=n
for j in range(k):
    c,i=0,0
    while m>0:
        c+=(m%10)*8**i
        i+=1
        m//=10
    cc,i=0,0
    while c>0:
        cc+=(c%9)*10**i
        i+=1
        c//=9
    ccc,i=0,0
    while cc>0:
        v=cc%10
        if v==8:
            ccc+=5*10**i
        else:
            ccc+=v*10**i
        i+=1
        cc//=10
    m=ccc
print(m)