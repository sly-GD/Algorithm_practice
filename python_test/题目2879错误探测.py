n=int(input())
arr=[]
a,b=[],[]
for i in range(n):
    arr.append(list(map(int,input().split())))
    if not arr[i].count(1)%2==0:
        a.append(i)
for i in range(n):
    x=0
    for j in range(n):
        if arr[j][i]==1:
            x+=1
    if not x%2==0:
        b.append(i)
if len(b)>1 or len(a)>1:
    print('Corrupt')
elif len(a)==0 and len(b)==0:
    print('OK')
else :
    print(a[0]+1,b[0]+1)
