# iridescent_sly time:17:30 date:2024/5/11
from collections import deque

n, k = map(int, input().split())
s = [list(input()) for i in range(n)]
vis = [[0 for _ in range(n)] for _ in range(n)]
q = deque([(2, 2, 2, 0)])
vis[2][2] = 1
dirt = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def f(x):
    if x < k:
        return 2
    elif x < 2 * k:
        return 1
    else:
        return 0


def check(x, y, z):
    for i in range(x - z, x + z + 1):
        for j in range(y - z, y + z + 1):
            # print(i, j)
            if s[i][j] == '*':
                return False
    return True


def check1(x, y, z):  # 检查标记
    for i in range(x - z, x + z + 1):
        for j in range(y - z, y + z + 1):
            if s[i][j] == '*':
                return False
    return True


def bfs():  # 广度搜索，扩散每一个点。利用队列。需要记录每一个搜索过的点
    while q:
        x, y, zhuangTai, cnt = q.popleft()
        if x == n - 3 and y == n - 3:
            print(cnt)
        if zhuangTai != 0:
            '''原地不动的状态，需要把新的时间点再入队。'''
            q.append((x, y, f(cnt + 1), cnt + 1))
        for i in range(4):
            nextX = x + dirt[i][0]
            nextY = y + dirt[i][1]
            # print('zheli', nextX, nextY)
            if nextX - zhuangTai >= 0 and nextX + zhuangTai < n and nextY - zhuangTai >= 0 and nextY + zhuangTai < n and \
                    vis[nextX][nextY] == 0:
                if check1(nextX, nextY, zhuangTai):
                    q.append((nextX, nextY, f(cnt + 1), cnt + 1))
                    vis[nextX][nextY] = 1


bfs()
