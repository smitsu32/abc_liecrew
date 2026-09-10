s=input()
x,used=[],set()
for i in range(len(s)):
    if s[i]=='(':
        x.append(s[i])
    elif s[i]==')':
        while x[-1]!='(':
            used.discard(x.pop())
        x.pop()
    else:
        if s[i] in used:
            print('No')
            exit()
        x.append(s[i])
        used.add(s[i])
print('Yes')