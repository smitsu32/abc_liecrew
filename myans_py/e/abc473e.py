n,k=map(int,input().split())
a=list(map(int,input().split()))

lst={0:0} #1個前の累積和iのidx
ans,l,sm=0,0,0 #答、左端、累積和modk
for i in range(n): #右端で区間スケジューリング問題
    sm=(sm+a[i])%k
    if sm in lst and lst[sm]>=l: #(sm[l]==sm[r]なら[l,r]分割でスコア+1)
        ans+=1
        l=i
    lst[sm]=i #剰余smの最終値更新

print(ans)