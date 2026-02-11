# iridescent_sly time:18:50 date:2024/5/18
n,m=map(int,input().split())
mx=[0]*110
sh=[[0]*(n+1) for i in range(m+1)]
for i in range(1,n+1):
    a=list(map(int,input().split()))
    for j in range(1,a[0]+1):
        sh[a[j]][i]=1
        mx[a[j]]+=1
for i in range(1,m+1):
    print(sh[i].count(1),mx[i])
