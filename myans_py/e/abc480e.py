import math # factorial(n):https://qiita.com/AkariLuminous/items/1b2e964ebabde9419224
n=int(input())

ans=0
# テスト2が間に合わないのでk=3だけ愚直にやる
for i in range(1,10**6+1):
    if i*(i+1)*(i+2)>n:
        break
    # 解の公式 (i+d)*(i+2d)=m (i*を右辺に、m=n/i)
    # ->  d = sqrt(i*i+8*i)-3*m//4 (d>0)
    ans+=(math.isqrt(i**2+8*n//i)-3*i)//4

for l in range(4,60): #2^60>10^18
    if math.factorial(l)>n:
        break
    
    for i in range(1,10**6+1): # (10^18)^1/3
        ok,ng=0,n+1 #二分探索で長さlの最大公比を調べる
        while abs(ok-ng)>1:
            mid=(ok+ng)//2
            p=1 
            for j in range(l):
                p*=i+mid*j
                if p>n: break
            if p<=n:
                ok=mid
            else:
                ng=mid
        if ok==0: break
        ans+=ok

print(ans)