arr=list(map(int,input().split()))
n=int(input())
x=0
for i in arr:
    if i<=n+30:
        x+=1
print(x)
          
