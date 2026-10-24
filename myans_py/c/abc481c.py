from collections import defaultdict
q=int(input())
d=defaultdict(int)
lst=1
for _ in range(q):
    s=input()
    if d[s]==0:
        d[s]=lst
        print(lst)
        lst+=1
    else:
        print(d[s])