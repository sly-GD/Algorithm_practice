
n,m,k=map(int,input().split())
a=[[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    a[i]=[0]+list(map(int,input().split()))

s=[[0]*(m+1) for i in range(n+1)]
s[0][0]=a[0][0]

for i in range(1,n+1):
    #s[i][0]=s[i-1][0]+a[i][0]
    for j in range(1,m+1):
        #s[0][j]=s[0][j-1]+a[0][j]
        s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i][j]

def getSum(i, j, u, v, p):
    return p[u][v] - p[u][j - 1] - p[i - 1][v] + p[i - 1][j - 1]




for i in range(1,n+1):#上边界
    for j in range(i,n+1):#下边界
        col_l=1
        for col_r in range(1,m+1):
            while col_l<=col_r and s[j][col_r]-s[j][col_l-1]-s[i-1][col_r]+s[i-1][col_l-1]>k:
                col_l+=1
            if col_l<=col_r:
                ans+=col_r-col_l+1



'''
for i in range(n-1,-1,-1):    
    for j in range(m-1,-1,-1):
        if s[i][j]-s[i][j-1]<=k:
            ans+=1

for j in range(m-1,-1,-1):    
    for i in range(n-1,-1,-1):
        if s[i][j]-s[i-1][j]<=k:
            ans+=1

for i in range(1,n):
    for j in range(1,m):
        if a[i][j]<=k:
            ans+=1
if a[1][1]<=k:
    ans+=1
'''

print(ans)
