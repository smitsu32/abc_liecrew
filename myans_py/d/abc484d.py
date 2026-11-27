n=int(input())
a=list(map(int,input().split()))

#解説AC: [l,r]をある条件で縮められれば答えも異なる → 数え上げ
cnt=[0]*n
ans=1 #初期a
for r in range(n):
    if a[r]!=a[r-1]: #r=r-1なら右シフトしても同じ = r-1に縮められる
        ans+=r-cnt[a[r]-1]
    cnt[a[r]-1]+=1

print(ans)