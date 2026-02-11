# # iridescent_sly time:16:01 date:2024/5/22
# import sys
#
# n, m = map(int, input().split())
# a = [0] + list(map(int, input().split()))
# g = {}
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     z += a[y]
#     if x not in g.keys():
#         g[x] = {y: z}
#     else:
#         g[x].update({y: z})
# # for _ in range(1, n + 1):
# #     if _ not in g.keys():
# #         g.update({_: {1: sys.maxsize}})
# start = 1
# goal = n
#
# min_dis = None  # 最短路径长度
# parent = {start: None}  # 存储父子节点关系，键为子节点，值为父节点
# '''
# open list 中存放那些已经访问的从该节点到起点有路径的结点（有路径但不一定是最优路径）。
# close list 中存放那些已经找到最优路径的结点。
# parent 存放结点的父子关系，方便后面路径回溯。
# '''
# open_list = {}
# closed_list = {}
# open_list[start] = 0
# try:
#     while True:
#         if open_list is None:
#             break
#         # 取出距离最小的点
#         distance, min_node = min(zip(open_list.values(), open_list.keys()))
#         open_list.pop(min_node)
#
#         closed_list[min_node] = distance
#         #print(g)
#         if min_node == goal:
#             min_dis = distance
#             shortest_path = [goal]
#             father_node = parent[goal]
#             while father_node != start:
#                 shortest_path.append(father_node)
#                 father_node = parent[father_node]
#             shortest_path.append(start)
#             # print(shortest_path[::-1])
#             print(min_dis - a[n])  # 本题需要减去最后一个城市的隔离时间
#
#         for node in g[min_node].keys():  # 遍历当前节点的邻接节点
#             if node not in closed_list.keys():  # 不在closed_list中
#                 if node in open_list.keys():  # 在open_list中
#                     if g[min_node][node] + distance < open_list[node]:
#                         open_list[node] = g[min_node][node] + distance
#                         parent[node] = min_node
#                 else:
#                     open_list[node] = g[min_node][node] + distance
#                     parent[node] = min_node
# except:
#     pass

import heapq
from collections import defaultdict, deque

maxn = 100005
inf = 0x3f3f3f3f

n, m = map(int, input().split())
add = [0] * (n + 1)
dis = [inf] * (n + 1)
vis = [False] * (n + 1)
G = defaultdict(list)
x=list(map(int,input().split()))
for i in range(1, n + 1):
    add[i] = x[i-1]

for _ in range(m):
    a, b, len_ = map(int, input().split())
    # 注意这里要同时添加两个方向的边，并且加上目标节点的点权
    G[a].append((b, len_ + add[b]))
    G[b].append((a, len_ + add[a]))
print(G)

def dijkstra():
    dis[1] = 0
    pq = [(0, 1)]  # 使用元组作为heapq的键值对，其中第一个元素为距离，第二个为节点
    heapq.heapify(pq)

    while pq:
        cost, u = heapq.heappop(pq)
        if vis[u]:
            continue
        vis[u] = True

        for v, new_cost in G[u]:
            if dis[v] > dis[u] + new_cost:
                dis[v] = dis[u] + new_cost
                heapq.heappush(pq, (dis[v], v))


dijkstra()
print(dis[n] - add[n])  # 终点不用隔离