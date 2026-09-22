n=int(input())
a,b,c=map(int,input().split())

ans=10**9+1
for i in range(10**4):
    for j in range(10**4):
        kyen=n-i*a-j*b
        if kyen<0: break
        
        if kyen%c==0:
            ans=min(ans,i+j+kyen//c)
    
    if n-i*a<0: break

print(ans)