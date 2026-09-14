h,w=map(int,input().split())
c=[input() for i in range(h)]

f=[[0]*(w+1) for i in range(h+1)] #一個外まで定義(分岐減る)
for i in range(h-1,-1,-1): #右下から探索
    for j in range(w-1,-1,-1):
        if c[i][j]=='#':
            f[i][j]=0
        else:
            f[i][j]=max(f[i+1][j],f[i][j+1])+1
print(f[0][0])