n,k=map(int, input().split())

ab=[]
# ai-bi < bi より差分とbiを同時ソート
for i in range(n):
    ai,bi=map(int, input().split())
    ab.append(ai-bi)
    ab.append(bi)
ab.sort(reverse=True)

ans=sum(ab[:k])
print(ans)