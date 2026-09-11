# upsolve 公式解説→gpt
n,x,y=map(int,input().split())
a=list(map(int,input().split()))

sx,sy={a[0]},{0} #到達可能点のset
for i in range(1,n):
    if i%2==0: #x
        nx=set()
        for u in sx:
            nx.add(u+a[i])
            nx.add(u-a[i])
        sx=nx #前後に更新
    else: #y
        ny=set()
        for u in sy:
            ny.add(u+a[i])
            ny.add(u-a[i])
        sy=ny
print('Yes' if x in sx and y in sy else 'No')