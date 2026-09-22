from bisect import bisect_left,bisect_right

n=int(input())
a=sorted(list(map(int,input().split())))

for _ in range(int(input())):
    b=int(input())
    i=bisect_left(a,b)
    if 0<i<n:
        print(min(b-a[i-1],a[i]-b))
    elif i==0:
        print(a[0]-b)
    else:
        print(b-a[-1])