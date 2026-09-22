n=int(input())

used=set()
for i in range(n):
    s=input()
    if s not in used:
        print(i+1)
        used.add(s)