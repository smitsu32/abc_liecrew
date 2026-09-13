from collections import deque
n=int(input())
s=input()

ans=deque([n]) #逆順で考える
for i in range(n-1,-1,-1):
    if s[i]=='R':
        ans.appendleft(i)
    else:
        ans.append(i)
print(*ans)