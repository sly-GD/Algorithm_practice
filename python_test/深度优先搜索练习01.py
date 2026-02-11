lst=[
    [10,1,3],
    [2,3,4],
    [1,0,1]
]
m,n=3,3
def dfs(i,j,val):
    if i<0 or i==m:
        return 0
    if j<0 or j==n:
        return 0
    if lst[i][j]>=val:
        return 0

    if (i,j) in dp:
        return dp[(i,j)]
    
    res=1 #表示本身的一格
    res=max(res,1+dfs(i-1,j,lst[i][j]))#向上
    res=max(res,1+dfs(i+1,j,lst[i][j]))
    res=max(res,1+dfs(i,j-1,lst[i][j]))
    res=max(res,1+dfs(i,j+1,lst[i][j]))
    dp[(i,j)]=res
    return res


dp={}

for x in range(n):
    for y in range(m):
        print(dfs(x,y,100),end=' ')# 初始值要给大一点
        
    print()
print(max(dp.values()))
