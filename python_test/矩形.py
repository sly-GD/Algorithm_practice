n=int(input())
a=list(map(int,input().split()))
cnt=0
res=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            res=max(res,a[i]*(j-i))
            print(res)
            break
print(res)
