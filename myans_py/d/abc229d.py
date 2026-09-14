s=input()
k=int(input())
n=len(s)

c=[0]
for i in range(n):
    c.append(c[-1]+(1 if s[i]=='.' else 0))

ans,r=0,0
for l in range(1,n+1): #尺取り
    while r<=n and c[r]-c[l-1]<=k:
        r+=1
    ans=max(ans,r-l)
print(ans)