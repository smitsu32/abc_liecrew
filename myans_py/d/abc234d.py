x=int(input())

l=[]
for i in range(1,10): #初項
    for j in range(-9,10): #公比
        li=[i]
        l.append(i)
        now=i
        for k in range(17): #項数
            now+=j
            if not 0<=now<10:
                break
            li.append(now)
            nn=''
            for dn in li:
                nn+=str(dn)
            l.append(int(nn))
l.sort()
for i in l:
    if i>=x:
        print(i)
        exit()