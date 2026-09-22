h,w=map(int, input().split())

# イルミネーション全体に完全に含まれる縦2×横2がないとき 
if h==1 or w==1:
    ans=max(h,w)
else:
    ans=((h+1)//2)*((w+1)//2)
print(ans)