n=int(input())
a=list(map(int, input().split()))
t=[0]*n #最後の個別更新時間(全体更新基準)
nt,na=0,0 #全体更新
for _ in range(int(input())):
    q=input().split()
    if q[0]=='1':
        na,nt=int(q[1]),nt+1
    elif q[0]=='2':
        i,x=int(q[1])-1,int(q[2])
        if t[i]<nt:
            a[i]=na+x
            t[i]=nt
        else:
            a[i]+=x
    else:
        i=int(q[1])-1
        if t[i]<nt:
            a[i],t[i]=na,nt
        print(a[i])