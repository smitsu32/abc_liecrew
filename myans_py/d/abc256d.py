n=int(input())
im=[0]*(2*10**5+2) #imos法
for i in range(n):
    l,r=map(int,input().split())
    im[l]+=1
    im[r]-=1 #半開

now,ans=0,-1
for i in range(len(im)):
    if now+im[i]>0 and now==0: #更新して正
        ans=i
    now+=im[i]
    if now==0 and ans!=-1: #更新して0
        print(ans,i)
        ans=-1