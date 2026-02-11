# iridescent_sly time:21:44 date:2024/5/28
from collections import deque

n = int(input())
N = 100001
G = [[] * N for _ in range(N)]
vis = [False] * N
rudu = [0] * N

for _ in range(n):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)
    rudu[x] += 1
    rudu[y] += 1  # 无向图

q = deque()
'''在环上的点必定有两端入度，不在换上的点也可能有2度
不过必定有尽头，
'''
for _ in range(n):
    if rudu[_] == 1:
        q.append(_)
        vis[_] = True

while q:
    u = q.popleft()
    # print('第',u,end=' ')
    for i in range(len(G[u])):
        # print(i,end=' ')
        v = G[u][i]
        rudu[v] -= 1
        if rudu[v] == 1:
            q.append(v)
            vis[v] = True
res = []
for i in range(1, n + 1):
    if not vis[i]:
        res.append(i)

print(*res,end='')
