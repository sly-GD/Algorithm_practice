n=int(input())
a=list(map(int,input().split()))

a.sort(reverse=True)
cnt=0
for i in a:
    n=n-i
    cnt+=1
    print(n)
    if n<0:
        break


print(cnt)
