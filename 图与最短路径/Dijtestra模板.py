# # iridescent_sly time:15:53 date:2024/5/22
'''

dijkstra算法带有负权的图不可用
'''


class edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w


n, m, s = map(int, input().split())
N = int(1e5)
e = [[]*N for _ in range(N)]
d = [float('inf')] * N
vis = [False] * N
pre=[0]*N  # 记录前驱点



for _ in range(m):
    a, b, w = map(int, input().split())
    e[a].append(edge(b, w))


def dijkstra(s):
    d[s] = 0
    for i in range(1, n + 1):  # 枚举每个点
        u = 0
        '''选秀，第一次选源点'''
        for j in range(1, n + 1):  # 枚举每个点
            if not vis[j] and d[j] < d[u]:  # 如果该点已经加入集合，则跳过
                u = j  # 选一个距离最小的点
        vis[u] = True  # 节点u出圈
        for x in e[u]:
            v = x.v
            w = x.w
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                pre[v]=u


'''
堆优化的，dijkstra算法
'''
import heapq

'''
heapq.heappush(q,item)
heapq.heappop(q)  默认小根堆
heapq.heapify(list)   对list进行堆化
'''
q = []


def dijkstra_heapq(s):
    d[s] = 0
    heapq.heappush(q, [0, s])  # 源点压入队列
    while q:
        print(q)
        t = heapq.heappop(q)

        u = t[1]

        if vis[u]:  # 凡是出队过的点都无需再次入队
            continue
        vis[u]=True

        for i in e[u]:
            print(i.v,i.w)
            v=i.v
            w=i.w
            if d[v]>d[u]+w:
                d[v]=d[u]+w
                pre[v]=u
                heapq.heappush(q,[d[v],v])

def dfs_path(u):
    if u==s:
        print(u,end=' ')
        return
    dfs_path(pre[u])
    print(u,end=' ')

dijkstra_heapq(s)
# dijkstra(s)
for i in range(1,n+1):
    print(d[i])
dfs_path(2)
# class Dijkstra:
#     def __init__(self, graph, start, goal):
#         self.graph = graph      # 邻接表
#         self.start = start      # 起点
#         self.goal = goal        # 终点
#
#         self.open_list = {}     # open 表
#         self.closed_list = {}   # closed 表
#
#         self.open_list[start] = 0.0     # 将起点放入 open_list 中
#
#         self.parent = {start: None}     # 存储节点的父子关系。键为子节点，值为父节点。方便做最后路径的回溯
#         self.min_dis = None             # 最短路径的长度
#
#     def shortest_path(self):
#
#         while True:
#             if self.open_list is None:
#                 print('搜索失败， 结束！')
#                 break
#             distance, min_node = min(zip(self.open_list.values(), self.open_list.keys()))      # 取出距离最小的节点
#             self.open_list.pop(min_node)                                                       # 将其从 open_list 中去除
#
#             self.closed_list[min_node] = distance                  # 将节点加入 closed_list 中
#
#             if min_node == self.goal:                              # 如果节点为终点
#                 self.min_dis = distance
#                 shortest_path = [self.goal]                        # 记录从终点回溯的路径
#                 father_node = self.parent[self.goal]
#                 while father_node != self.start:
#                     shortest_path.append(father_node)
#                     father_node = self.parent[father_node]
#                 shortest_path.append(self.start)
#                 print(shortest_path[::-1])                         # 逆序
#                 print('最短路径的长度为：{}'.format(self.min_dis))
#                 print('找到最短路径， 结束！')
#                 return shortest_path[::-1], self.min_dis			# 返回最短路径和最短路径长度
#
#             for node in self.graph[min_node].keys():               # 遍历当前节点的邻接节点
#                 if node not in self.closed_list.keys():            # 邻接节点不在 closed_list 中
#                     if node in self.open_list.keys():              # 如果节点在 open_list 中
#                         if self.graph[min_node][node] + distance < self.open_list[node]:
#                             self.open_list[node] = distance + self.graph[min_node][node]         # 更新节点的值
#                             self.parent[node] = min_node           # 更新继承关系
#                     else:                                          # 如果节点不在 open_list 中
#                         self.open_list[node] = distance + self.graph[min_node][node]             # 计算节点的值，并加入 open_list 中
#                         self.parent[node] = min_node               # 更新继承关系
#
#
# if __name__ == '__main__':
#     g = {'1': {'2': 2, '4': 1},
#          '2': {'4': 3, '5': 11},
#          '3': {'1': 4, '6': 5},
#          '4': {'3': 2, '6': 8, '7': 4, '5': 2},
#          '5': {'7': 6},
#          '7': {10000:100000}
#          }
#     start = '1'
#     goal = '6'
#     dijk = Dijkstra(g, start, goal)
#     dijk.shortest_path()
