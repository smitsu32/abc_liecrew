n,q=map(int, input().split())
a=list(map(int, input().split()))

offset=0
for i in range(q):
    t,x,y=map(int, input().split())
    x-=1; y-=1
    if t==1:
        a[(x+offset)%n],a[(y+offset)%n]=a[(y+offset)%n],a[(x+offset)%n]
    elif t==2:
        offset-=1 #右シフト→始点1のときnに,2のとき1になる→-1
    else:
        print(a[(x+offset)%n])