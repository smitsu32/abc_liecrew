n,x=map(int,input().split())
s=input()

y=[]
while x>0:
    y.append(x%2)
    x//=2
y=y[::-1]

for i in range(n):
    if s[i]=='U':
        y.pop()
    elif s[i]=='R':
        y.append(1)
    else:
        y.append(0)

ans=0
for i in range(len(y)):
    ans=ans*2+y[i]
print(ans)