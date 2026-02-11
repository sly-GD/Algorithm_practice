m,n=map(int,input().split())
arr=[]
for i in range(m):
    arr.append(list(map(int,input().split())))

#arr=[int(x) for x in arr]
    
s=0
for i in range(m):
    if i==0 or i==m-1:
        s+=sum(arr[i])
        '''for j in range(n):
            s+=int(arr[i][j])
        '''
    else :
        s+=int(arr[i][0])+int(arr[i][n-1])
print(s)
