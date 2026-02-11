a=[]
rows=[]
cols=[]
for i in range(5):
    a.append(list(map(int,input().split())))
    rows.append(max(a[i]))
for j in range(5):
    x=a[0][j]
    for i in range(5):
        if x>a[i][j]:
            x=a[i][j]
    cols.append(x)
flag=1
for i in range(5):
    for j in range(5):
        if a[i][j]==rows[i] and a[i][j]==cols[j]:
            print(i+1,j+1,a[i][j])
            flag=0
if flag==1:
    print('not found')
                
