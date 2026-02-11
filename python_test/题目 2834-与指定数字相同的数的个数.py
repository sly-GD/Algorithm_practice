n=int(input())
arr=list(map(int,input().split()))
x=int(input())
a=0
for i in arr:
    if x==i:
        a+=1
print(a)
