# iridescent_sly time:21:02 date:2024/6/1
n, m = map(int, input().split())
import heapq
from collections import defaultdict

N = 100010
e=[]
# e = defaultdict(list)
vis = [False] * N
p = [0] * N


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


for _ in range(m):
    u, v, w = map(int, input().split())
    e.append(Edge(u, v, w))
    #print(e[_])
e.sort(key=lambda x: x.w)

'''初始化并查集'''
for _ in range(1, n + 1):
    p[_] = _
x = 0
'''枚举每一条边'''
for i in range(m):
    u = e[i].u;
    v = e[i].v;
    w = e[i].w
    u = find(u);
    v = find(v)  # 分别查找u、v的祖宗节点
    if u != v:  # u和v不在一个集合
        x = max(x, w)
        p[u] = v  # 合并集合

    if find(1) == find(n):
        break

print(x)

# def dij():
#     x = 0
#     q = e[1][:]
#     heapq.heapify(q)
#     # print(q)
#     while q and vis[n] == False:
#         t = heapq.heappop(q)
#         # print(t)
#         di = t[0]
#         node = t[1]
#         # print(di,node)
#         if vis[node] == False:
#             x = max(x, di)
#             vis[node] = True
#             for ne in e[node]:
#                 v = ne[1]
#                 w = ne[0]
#                 if vis[v] == False:
#                     heapq.heappush(q, [w, v])
#     print(x)
#
#
# dij()
