# iridescent_sly time:21:48 date:2024/5/2
n=int(input())
a=[[] for i in range(n)]
for i in range(n):
    a[i]=list(map(int,input().split()))

r=int(10**12)
l=0

def check(x):   #n个区间不一定是递增的
    L=(-x);R=x
    for i in range(len(a)):
        if a[i][0]>R or a[i][1]<L:
            return False
        L=max(a[i][0]-x,L-x)
        R=min(a[i][1]+x,R+x)
    return True

ans=0
while l<=r:     #注意是大的一边满足还是小的一边满足，决定r，l的位置
    mid=(l+r)//2
    if check(mid):
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)
