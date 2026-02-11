# iridescent_sly time:19:31 date:2024/5/28
a=list(map(int,input().split()))
h=int(input())
cnt=0
for i in a:
    if i<=h+30:
        cnt+=1
print(cnt)