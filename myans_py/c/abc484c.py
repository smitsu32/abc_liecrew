n=int(input())
a,b=list(map(int,input().split())),list(map(int,input().split()))

if a==b:
    print('Yes')
    exit()

l,r=0,n-1
while a[l]==b[l]:
    l+=1
while a[r]==b[r]:
    r-=1

#解説AC：異なる区間だけ右シフトと左シフトしたら等しくなるか？
aa,bb=a[l:r+1],b[l:r+1]
if aa[1:]+[aa[0]]==bb or [aa[-1]]+aa[:-1]==bb:
    print('Yes')
else:
    print('No')