# iridescent_sly time:20:32 date:2024/5/28
from collections import deque

x1, y1 = map(int, input().split())
n = 100
dx = [-1, -2, -2, -1, -2, -2, 1, 2, 2, 1, 2, 2]
dy = [-2, -1, -2, 2, 1, 2, -2, -1, -2, 2, 1, 2]

vis = [[False] * n for _ in range(n)]


class NOde:
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step
def bfs(x,y):
    vis[x][y]=True
    q=deque()
    q.append(NOde(x,y,0))
    while q:
        #print('jin')
        u=q.popleft()
        # if vis[u.x][u.y]:
        #     continue
        for i in range(len(dx)):
            #print(i)
            nx=u.x+dx[i]
            ny=u.y+dy[i]
            if 0<=nx<=n and 0<=ny<=n and not vis[nx][ny] :
                #print('zhe')
                q.append(NOde(nx,ny,u.step+1))
                vis[u.x][u.y]=True
            if nx == x1 and ny == y1:
                print(u.step+1)
                return

bfs(1,1)

x1, y1 = map(int, input().split())
vis=[[False]*n for _ in range(n)]
bfs(1,1)