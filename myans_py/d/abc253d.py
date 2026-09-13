from math import gcd
n,a,b=map(int,input().split())

ans=(1+n)*n//2
aa,bb,ab=n//a,n//b,a*b//gcd(a,b)
cc=n//ab
a1,a2,a3=a*(1+aa)*aa//2,b*(1+bb)*bb//2,ab*(1+cc)*cc//2
print(ans-a1-a2+a3)