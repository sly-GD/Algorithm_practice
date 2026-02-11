# iridescent_sly time:12:23 date:2024/5/29
from collections import deque

N = int(1e3) + 10
M=N//2
dep = [0] * N
fa = [[0] * 20 for _ in range(N)]
'''
dep[u]存储u节点的深度
fa[u][i]存储u节点向上跳2^i层的祖先节点
'''
du = [0] * N
dist = [0] * N
n, m = map(int, input().split())
# print(n,m)
e = [[] * M for _ in range(M)]  # 存储邻接节点

'''打表，ST表'''


##print(e[:10])
def dfs(u, father):
    # print(u,father)
    ''' u表示当前节点，father表示当前节点父节点 '''
    dep[u] = dep[father] + 1
    dist[u] = dist[father] + du[u]
    '''倍增递推，从小到大枚举'''
    fa[u][0] = father
    for i in range(1, 20):  # 1-20表示i 的幂
        fa[u][i] = fa[fa[u][i - 1]][i - 1]
    # print(e[u])
    for v in e[u]:
        if v != father:
            dfs(v, u)

#
# def bfs(root):
#     dep[0] = 0
#     dep[root] = 1
#     q = deque()
#     q.append(root)
#     while q:
#         u = q.popleft()


'''二进制拆分，从大到小枚举'''


def lca(u, v):  # 目标两点
    #print("u,v",u,v)
    if dep[u] < dep[v]:
        u, v = v, u
    #print('交换',u,v)
    for i in range(19, -1,-1):
        if dep[fa[u][i]] >= dep[v]:
            #print("zheil")
            u = fa[u][i]  # u不断向上跳
#    print(v,u)

    if u == v:
        return v

    ''' 跳到同层之后，两个一起跳'''

    for i in range(19, -1,-1):
        '''防止跳出界，可设置哨兵'''
        if fa[u][i] != fa[v][i]:
            u = fa[u][i]
            v = fa[v][i]
    return fa[u][0]


for _ in range(1, n):
    x, y = map(int, input().split())
    e[x].append(y)
    e[y].append(x)
    du[x] += 1
    du[y] += 1
# print(e[:10])
dfs(1, 0)
#print(dep[1])

# for i in range(20):
#     print(fa[i][:10])

# print(dist[:10])
for _ in range(m):
    x, y = map(int, input().split())

    l = lca(x, y)
    #print(l)
    # if x == 1 or y == 1:
    #     print(dist[x] + dist[y] - 2 * dist[l])
    print(dist[x] + dist[y] - 2 * dist[l] + du[l])
