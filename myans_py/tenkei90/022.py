a,b,c=map(int,input().split())

# GCD: 最大公約数(=Greatest Common Divisor)
# ユークリッドの互除法
def euclid(x,y):
    while x>0 and y>0:
        if x>=y:
            x%=y
        else:
            y%=x
    return max(x,y)

gcd=euclid(a,euclid(b,c))

ans=a//gcd-1 + b//gcd-1 +c//gcd-1
print(ans)