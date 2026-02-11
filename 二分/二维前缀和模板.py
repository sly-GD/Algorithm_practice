# iridescent_sly time:20:04 date:2024/5/31
n,m,k=map(int,input().split())
# a=[[]*1010 for _ in range(1010)]
a=[]*1010
a.append([0]*(m+1))
s=[[0]*1010 for _ in range(1010)]
for _ in range(n):
    t=list(map(int,input().split()))
    a.append([0]+t)
#     print(a[_])
# print(a)
for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j]
    # print(s[i][:20])
for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    ans=s[x2][y2]-s[x2][y1-1]-s[x1-1][y2]+s[x1-1][y1-1]
    print(ans)