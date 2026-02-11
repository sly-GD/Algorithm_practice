# iridescent_sly time:21:33 date:2024/5/27
"""有向无环图"""

'''拓扑排序的目的是将所有节点排序，
使得排在前面的节点不能依赖排在后面的节点
'''
"""Kahn算法
Kahn 算法基于以下思想实现：
1. 一条入边即为一条依赖，有多少入度，就有多少个依赖。
2. 对于所有未访问的节点，我们必须从入度为 的节点开始访问。
3. 访问一个节点后，其节点的出边所造成的依赖消失，该出边对应的入
度就减少。
因此，Kahn 算法实现步骤如下：
1. 初始状态下，集合 装着所有入度为 的点， 是一个空列表。
2. 每次从 中取出一个点 （可以随便取）放入 , 然后将 的所有边
删除。对于边 ，若将该边删除后点
的入度变为 ，则将 放入 中。
3. 不断重复以上过程，直到集合 为空。
4. 检查图中是否存在任何边或者还有节点没有被访问过，如果有，那么
这个图一定至少存在一条环路，否则返回 , 中顶点的顺序就是拓
扑排序的结果。

"""

from collections import deque

N = int(1e3) + 5
n = 0
m = 0
x = 0
y = 0
'''
n:节点数
m：边数

'''
G = [[]] * N  # 邻接表表示图
q = deque()  # 双端队列
ans = []  # 存放排序结果
cnt = [0] * N  # 记录每个节点的入度
tpc = 0  # 已访问节点数量


def Kahn():
    global tpc
    """将入度为0的点入队"""
    for i in range(1, n + 1):
        if cnt[i] != 0:
            q.append(i)
    while q:
        u = q.popleft()
        tpc += 1  # 统计访问过节点数量
        ans.append(u)  # 压入已访问节点
        for i in range(len(G[u]), -1, -1):
            v = G[u][i]
            cnt[v] -= 1  # 入度-1
            if not cnt[v]:
                q.append(v)
    return tpc == n  # 如果所有节点都访问了，说明不存在环


# n,m=map(int,input().split())
'''构建图'''
while m:
    x, y = map(int, input().split())
    G[x].append(y)
    cnt[y] += 1
    m -= 1

if not Kahn():
    print('loop exist.')
else:
    print('sort result.')
    for i in range(len(ans)):
        print(ans[i], end=' ')
