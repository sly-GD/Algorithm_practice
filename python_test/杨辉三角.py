n=9
x,y=7,2

a=[[1] * n for i in range(n)]

for i in range(2,n):
    for j in range(1,i):
        a[i][j]=a[i-1][j]+a[i-1][j-1]


res1=a[x-1][y-1]

print(res1)

res2=0
for i in range(x-1,y-1-1,-1):
    res2+=a[i][y-1]
print(res2)
for i in a:
    print(i)
