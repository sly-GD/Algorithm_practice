# iridescent_sly time:13:20 date:2024/5/27
n,m=map(int,input().split())
A=[]
B=[]
for _ in range(n):
    x,y,z=map(str,input().split())
    if z=='A':
        A.append((int(x),int(y)))
    else:
        B.append((int(x),int(y)))
for _ in range(m):
    c,a,b=map(int,input().split())
    flag=0
    if c+a*A[0][0]+b*A[0][1]>0:
        flag=1
    else:
        flag=0
    for i in range(len(A)):
        x=c+a*A[i][0]+b*A[i][1]
        if (x>0 and flag==0) or (x<0 and flag==1):
            print('No')
            flag=100
            break
    if flag==100:
        continue
    flag = 0
    if c + a * B[0][0] + b * B[0][1] > 0:
        flag = 1
    else:
        flag = 0
    for i in range(len(B)):
        x = c + a * B[i][0] + b * B[i][1]
        if (x > 0 and flag == 0) or (x < 0 and flag == 1):
            flag=100
            print('No')
            break
    if flag==100:
        continue
    print("Yes")
