a=[
    '1234',
    '4321',
    '3100',
    '0000'
    ]

a=[[int(x) for x in row] for row in a]
'''for  row in a:
        print(row)
print()
b=list(zip(*a))
for  row in b:
        print(row)
print()'''
def valid(x,y,num):
    if num in a[x]:
        return False
    if num in list(zip(*a))[y]:   #zip()压缩行变列，zip(*)解压缩列变行
        return False

    #验证宫格
    ax=x//2;ay=y//2
    for i  in range(2):
        for j in range(2):
            nx,ny=ax*2+i,ay*2+j
            if num==a[nx][ny]:
                return False
    return True

cnt=0

def find():
    global cnt
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==0:
                for m in range(1,5,1):
                    if valid(i,j,m):
                        a[i][j]=m
                        find()
                        a[i][j]=0
                return
    print('found')
    cnt+=1
    for  row in a:
        print(row)

find()
print(cnt)

for  row in a:
        print(row)
