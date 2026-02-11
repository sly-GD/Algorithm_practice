n,m=4,4

a=[]
for i in range(n):
    a.append(list(map(str,input().split())))
cnt=0
def dfs(x,y):
    # global cnt
    if x<0 or x==n or y<0 or y==m:
        return
    if a[x][y]=='x':
        return
    else:
        #print("jinru",x,y)
        a[x][y]='x'
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        #a[x][y]='r'
    #cnt+=1
print(a)
for i in range(n):
    for j in range(m):
        if a[i][j]=='r':
            cnt+=1
            dfs(i,j)
print(cnt)
