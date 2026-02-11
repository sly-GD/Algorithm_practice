# iridescent_sly time:11:02 date:2024/5/30
'''

Bellman-Ford算法步骤
Bellman-Ford 算法采用动态规划（Dynamic Programming）进行设计，实
现的时间复杂度为O(V*E) ，其中V 为顶点数量，E 为边的数量。
Dijkstra 算法采用贪心算法（Greedy Algorithm）范式进行设计，普通实现
的时间复杂度为 O(E+VlogV)，若基于堆优化的最小优先队列实现版本则时间复
杂度为 。
'''
'''
Bellman-Ford 算法描述：
1. 创建源顶点 v 到图中所有顶点的距离的集合dis[] ，为图中的所有顶点
指定一个距离值，初始均为 ，源顶点距离为 ；
2. 计算最短路径，执行V-1 次遍历（松弛边）；
对于图中的每条边：如果起点 u的距离d 加上边的权值 w小于终点v
的距离d ，则更新终点 v的距离值d ；
3. 检测图中是否有负权边形成了环， 遍历图中的所有边， 
如果dis[e.u]+e.w<dis[e.v]，则说明存在环；
为什么要循环 n-1次？
因为最短路径肯定是个简单路径，不可能包含回路的。而图有 个点，又
不能有回路 所以最短路径最多 n-1边，又因为每次循环，至少松弛了一
条边 所以最多n-1 次就行了。
'''
'''
为什么Dijkstra无法处理负边，而Bellman-Ford可以处理负边？
Dijkstra本质上是一种贪心策略，当有负边存在时，局部最优无法带来全局
最优，贪心失效。
Bellman-Ford本质上是一种枚举策略，在求解s->0 的最短路径时，会计
算所有 s->b的不包含环路的路径，从中挑出权值和最小的路径。
SPFA 的核心原理和 Bellman-ford 算法是一样的，也是对点的松弛。只不过
它优化了复杂度，优化的原理很简单， 只有被松弛过的点才有可能去松弛
其他的点。优化的方法也很简单，用一个队列维护了可能存在新的松弛的
点，这样我们每次从这些点出发去寻找其他可以松弛的点加入队列。
SPFA 的代码也很短，实现起来难度很低，单单从代码上来看和普通的宽搜
区别并不大。
'''


class edge:
    def __init__(self, v, w):
        self.v = v  # 表示边的出点
        self.w = w  # 表示边权


N = int(1e5)
e = [[] * N for i in range(N)]  # 存储边集
d = [float('inf')] * N  # 存储距离 初始设为无穷大

n, m, root = map(int, input().split())

for _ in range(m):
    a, b, w = map(int, input().split())
    e[a].append([b, w])


def bellman_Ford(root):
    d[root] = 0
    flag = False  # 判断是否松弛
    for i in range(1, n + 1):  # 遍历n轮
        flag = False
        for j in range(1, n + 1):  # 每轮通过两个for遍历所以边
            if d[j] == float('inf'):  # 该点还没有被更新
                continue
            for x in e[j]:
                v = x[0]
                w = x[1]
                if d[v] > d[j] + w:
                    d[v] = d[j] + w  # 动态选最小
                    flag = True
        if not flag:
            break
    return flag  # if 第n轮==true 说明有环存在


if bellman_Ford(root):
    print('有环存在，判负环')
