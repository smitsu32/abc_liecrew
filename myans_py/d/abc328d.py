s=input()
l=[]

for i in s:
    l.append(i)
    while len(l)>=3 and l[-3:]==['A','B','C']:
        for _ in range(3):
            l.pop()
print(''.join(l))