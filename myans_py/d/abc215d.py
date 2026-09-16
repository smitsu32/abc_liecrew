n,m=map(int,input().split())
a=list(map(int,input().split()))
mx=10**5+1

def era(n): #素因数 n=6-> 6->1,2,3,6
    p=set()
    for i in range(2,int(n**0.5)+1):
        while n%i==0:
            n//=i
            p.add(i) #割り切れるなら
    if n>1:
        p.add(n)
    return p

p=[True]*mx
for i in a:
    for j in era(i): #素因数
        if p[j]:
            for k in range(j,mx,j): #aiの素因数の倍数を消す
                p[k]=False

ans=[]
for i in range(1,m+1):
    if p[i]: ans.append(i)
print(len(ans),*ans,sep='\n')