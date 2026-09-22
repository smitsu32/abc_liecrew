n=int(input())
sm1,sm2=[0]*(n+1),[0]*(n+1)

now1,now2=0,0
for i in range(n):
    c,p=map(int,input().split())
    if c==1:
        now1+=p
    else:
        now2+=p
    sm1[i+1]=now1
    sm2[i+1]=now2

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(sm1[b]-sm1[a-1],sm2[b]-sm2[a-1])