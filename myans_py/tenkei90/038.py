a,b=map(int, input().split())
aa,bb=a,b
INF=10**18

# lcm(a,b) = a*b / gcd(a,b)
while bb>0:
    aa,bb=bb,aa%bb
gcd=aa

lcm=a*b//gcd
if lcm>INF:
    print('Large')
else:
    print(lcm)