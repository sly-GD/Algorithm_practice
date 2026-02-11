n=int(input())

maindiag=[0 for i in range(2*n-1)]
subdiag=[0 for i in range(2*n-1)]
colum=[0 for i in range(n)]
rows=[0 for i in range(n)]

def printSolution():
    for i in range(n):
        for j in range(n):
            if rows[i]==j:
                 print("Q",end=' ')
            else :
                print("0",end=' ')
        print()
    print()

cnt=0

def search(row):
    global cnt
    for col in range(n):
        x=row;y=col
        if maindiag[x-y+n-1]==0 and subdiag[x+y]==0 and colum[y]==0:
            rows[x]=y   #用于存储该行放置的列
            maindiag[x-y+n-1]=1
            subdiag[x+y]=1
            colum[y]=1

            if row<n-1: #继续寻找下一行
                search(row+1)
            else :
                cnt+=1
                #printSolution()
               # print("found")

            maindiag[x-y+n-1]=0
            subdiag[x+y]=0
            colum[y]=0
            rows[x]=-1

search(0)
print(cnt)
