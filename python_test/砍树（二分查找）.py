n,m=map(int,input().split())

tree=list(map(int,input().split()))

l=0
r=max(tree)
#print(r)
res=0
def check(x):
    global res
    res=0
    for i in tree:
        temp=i-x
        if temp<0:
            continue
        else:
            res+=temp
    return res<m
x=0
while l<=r:
    #print(mid)
    mid=(l+r)//2
    if check(mid):
        r=mid-1
    else:
        x=mid
        l=mid+1
print(x)
