# iridescent_sly time:12:00 date:2024/5/29
N = int(5e5) + 10
dep = [0] * N
fa = [[0] * 20 for _ in range(N)]
'''
dep[u]存储u节点的深度
fa[u][i]存储u节点向上跳2^i层的祖先节点
'''

n = 0
m = 1

e = [[0] * N for _ in range(N)]  # 存储邻接节点

'''打表，ST表'''
def dfs(u, father):
    ''' u表示当前节点，father表示当前节点父节点 '''
    dep[u]=dep[father]+1
    '''倍增递推，从小到大枚举'''
    for i in range(1,20): # 1-20表示i 的幂
        fa[u][i]=fa[fa[u][i-1]][i-1]

    for v in e[u]:
        if v!=father:
            dfs(v,u)

'''二进制拆分，从大到小枚举'''
def lca(u,v): #目标两点
    if dep[u]>dep[v]:
        u,v=v,u

    for i in range(19,0):
        if dep[u]>=dep[v]:
            u=fa[u][i]  # u不断向上跳

    if u==v:
        return v

    ''' 跳到同层之后，两个一起跳'''

    for i in range(19,0):
        '''防止跳出界，可设置哨兵'''
        if fa[u][i]!=fa[v][i]:
            u=fa[u][i]
            v=fa[v][i]
    return fa[u][0]