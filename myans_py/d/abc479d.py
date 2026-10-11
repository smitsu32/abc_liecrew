n,q=map(int,input().split())
l=list(map(int,input().split()))
r=list(map(int,input().split()))
sr,sl=r[:],l[:]
for i in range(1,n-1):
    sr[i]=min(r[i],sr[i-1]) #累積和的に最適な戻りを格納
for i in range(n-3,-1,-1):
    sl[i]=min(sl[i+1],l[i])

for _ in range(q):
    s,t=map(int,input().split())
    s-=1
    if s<t:
        if s==0:
            print(r[s])
        else:
            print(min(r[s],l[s-1]+sr[s-1])) #直接行くか、戻って行くか← →
    else:
        if s==n-1:
            print(l[-1])
        else:
            print(min(l[s-1],r[s]+sl[s])) #直接戻るか、行って戻るか→ ←