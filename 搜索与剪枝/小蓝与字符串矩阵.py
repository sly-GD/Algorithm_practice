# iridescent_sly time:15:48 date:2024/5/12
ten = 'encent'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
N = 1010
a = [[''] * N for i in range(N)]
t = []
mk = {}
for i in range(1, n + 1):
    row = input()
    for j in range(1, m + 1):
        a[i][j] = row[j - 1]
        if a[i][j] == 't':
            t.append((i, j))

ans = 0


def dfs(x, y, now):
    global ans
    if now == 6:
        ans += 1
        return
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 1 <= xx <= n and 1 <= yy <= m and a[xx][yy] == ten[now]:
            dfs(xx, yy, now + 1)

for i in t:
    dfs(i[0],i[1],0)
print(ans)
