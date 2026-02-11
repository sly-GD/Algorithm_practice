t = int(input())

for _ in range(t):
    m,n,a,b=map(int,input().split())


    dirs=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

    board=[[0]*n for i in range(m)]
    cnt=0#路径数量

    def move(x,y,step):
        global cnt  
        if step==m*n:  #setp等于格子点数为走完一次的一种路径
            cnt+=1
            return
        for i in range(len(dirs)):
            next_x=x+dirs[i][0]
            next_y=y+dirs[i][1]
            '''for o in range(m):
                print(board[o])
            print()'''
            if next_x>=0 and next_x<=m-1 and next_y>=0 and next_y<=n-1 and board[next_x][next_y]==0:
               board[next_x][next_y]=1
               move(next_x,next_y,step+1)
               board[next_x][next_y]=0  # 这个坐标没有下一步可走，则回溯0

    board[a][b]=1
    move(a,b,1)
    print(cnt)
