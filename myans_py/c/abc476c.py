from sortedcontainers import SortedList
n=int(input())
a=list(map(int,input().split()))
sl=SortedList()
sl.add(a[0]); sl.add(a[1])
for i in range(n-2):
    sl.add(a[i+2])
    print(sl[-3])