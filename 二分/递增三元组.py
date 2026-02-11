# iridescent_sly time:21:20 date:2024/5/2
import bisect
n=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A.sort()
C.sort()
cnta=0
cntc=0
ans=0
for i in range(len(B)):
    cnta=bisect.bisect_left(A,B[i])
    cntc=n-bisect.bisect_right(C,B[i])
    ans+=cntc*cnta
print(ans)














'''
r=len(A)
l=0

def check(x):
    op=0
    


ans=0
while l<=r:
    mid=(l+r)//2
    if check(mid):
        ans=mid
        l=mid+1
    else:
        r=mid-1
print(ans)
'''