# iridescent_sly time:14:58 date:2024/5/12
from collections import deque

n, m = map(int, input().split())
N = 1010
a = [[''] * N for i in range(N)]
vis = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
d = [[float('inf')] * N for _ in range(N)]
sx, sy, ex, ey = 0, 0, 0, 0
c, v = [], []
outb = 0
for i in range(1, n + 1):
    row = input()
    for j in range(1, m + 1):
        a[i][j] = row[j - 1]
        if a[i][j] == 'S':
            sx, sy = i, j
        if a[i][j] == 'E':
            ex, ey = i, j
        if '1' <= a[i][j] <= '9':
            c.append(i)
            v.append(j)
#print(c, 'djk', v)


def bfs1(x, y):
    global vis, ex, ey, outb
    vis[x][y] = 1
    q = deque()
    q.append((x, y, 0))
    while q:
        p = q.popleft()
        if p[0] == ex and p[1] == ey:
            outb = p[2]
            break
        for i in range(4):
            xx = p[0] + dx[i]
            yy = p[1] + dy[i]
            if 1 <= xx <= n and 1 <= yy <= m and vis[xx][yy] == 0 and a[xx][yy] != 'T':
                vis[xx][yy] = 1
                q.append((xx, yy, p[2] + 1))


def bfs2(x, y):
    global vis
    vis[x][y] = 1
    q = deque()
    q.append((x, y, 0))
    while q:
        p = q.popleft()
        d[p[0]][p[1]] = p[2]
        for i in range(4):
            xx = p[0] + dx[i]
            yy = p[1] + dy[i]
            if 1 <= xx <= n and 1 <= yy <= m and vis[xx][yy] == 0 and a[xx][yy] != 'T':
                vis[xx][yy] = 1
                q.append((xx, yy, p[2] + 1))


bfs1(sx, sy)
vis = [[0] * N for _ in range(N)]
bfs2(ex, ey)

ans = 0
for i,j in map(lambda x,y:(x,y),c,v):

        #print(a[i][j])
        # if '1' <= a[i][j] <= '9':
        if d[i][j] <= outb:
            ans += int(a[i][j])
print(ans)
