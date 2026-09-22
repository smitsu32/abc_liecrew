n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()
# 順番を崩さないのが最小の距離（Greedy）
ans=0
for i in range(n):
    ans+=abs(a[i]-b[i])

print(ans)