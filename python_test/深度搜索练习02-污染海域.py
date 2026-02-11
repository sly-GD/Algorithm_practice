lst=[
    [1,1,0,0,0],
    [1,1,1,0,0],
    [1,0,0,0,0],
    [1,1,0,1,1]
    ]


m,n=4,5
'''def dfs(i,j,val):
    if i<0 or i==m:
        return 0
    if j<0 or j==n:
        return 0
    if lst[i][j]==0:
        return 0
    if lst[i][j]==1:
        lst[i][j]=0

    dfs(i-1,j,lst[i][j])
    dfs(i+1,j,lst[i][j])
    dfs(i,j+1,lst[i][j])
    dfs(i,j-1,lst[i][j])
    return 1

ans=0

for x in range(m):
    for y in range(n):
        #print(dfs(x,y,lst[x][y]),end='')
        if dfs(x,y,lst[x][y]):
            ans+=1
    #print()
print(ans)
'''



#优化后

def dfs(i,j):
    if i<0 or i==m or j<0 or j==n or lst[i][j]==0:
        return 0

    lst[i][j]=0#标记一下

    dfs(i-1,j)
    dfs(i+1,j)
    dfs(i,j-1)
    dfs(i,j+1)

ans=0

for x in range(m):
    for y in range(n):
        if lst[x][y]==1:
            dfs(x,y)
            ans+=1
print(ans)
