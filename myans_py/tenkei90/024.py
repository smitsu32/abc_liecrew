n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# mod2が等しい ＆ k>=総差
diff=0
for i in range(n):
    diff+=abs(a[i]-b[i])
    
if diff<=k and diff%2==k%2:
    print('Yes')
else:
    print('No')