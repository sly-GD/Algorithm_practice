# iridescent_sly time:19:56 date:2024/6/1
n,k=map(int,input().split())

a=list(map(int,input().split()))

cnt=0
w=0
for i in range(n):
    w+=a[i]
    if w>=k:
        cnt+=1
        w=0
        continue
if w>0:
    cnt+=1
print(cnt)