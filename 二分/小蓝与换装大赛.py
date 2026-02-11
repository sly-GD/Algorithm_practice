# iridescent_sly time:13:57 date:2024/5/3
n,m=map(int,input().split())
a=list(map(int,input().split()))
t=[[0,0]for i in range(n)]
def check(x):
    for i in range(n):
        t[i][0]=a[i]-x
        t[i][1]=a[i]+x
    t.sort(key=lambda x: x[1])
    ans=1
    f=t[0][1]
    for i in range(1,n):
        if t[i][0]>f:
            f=t[i][1]
            ans+=1
    return ans<=m

l=0
r=int(1e9)
ans=0
while l<=r:
    mid=(l+r)//2
    if check(mid):
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)