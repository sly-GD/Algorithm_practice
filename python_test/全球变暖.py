n=int(input())
a=[]
flag=[]
for i in range(n):
    a.append(input())
    flag.append([0]*len(a[i]))

def bfs(i,j):
    if i<0 or i>=n or j<0 or j>=len(a[0]):
        return False
    flag[i][j]=1

    if a[i-1][j]=='.' or a[i+1][j]=='.' or a[i][j+1]=='.' or a[i][j-1]=='.':
        x=list(a[i])
        x[j]='x'
        a[i]=''.join(x)
    


res=0
for i in range(n):
    for j in range(len(a[0])):
        if a[i][j]=='#':
            bfs(i,j)
for i in range(n):
    for j in range(len(a[0])):
        if a[i][j]=='#':
            res+=1
print(res)
