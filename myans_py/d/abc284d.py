def spf(n): #エラトステネスの篩
    mx=int(n**(1/3))+1 #t=p^2*q
    isp=[True]*mx
    isp[0],isp[1]=False,False
    for i in range(2,mx):
        if not isp[i]:
            continue
        for j in range(i**2,mx,i):
            isp[j]=False
    return isp,mx

for _ in range(int(input())):
    t=int(input())
    isp,n=spf(t)
    for i in range(n):
        if isp[i]:
            if t%(i**2)==0 and t%(t//(i**2))==0: # iが2乗
                print(i,t//(i**2))
                break
            elif t%i==0 and t%(t//i)==0: # iが1乗
                print(int((t//i)**0.5),i)
                break