'''# iridescent_sly time:15:38 date:2024/5/18
N = 110
M = 2 * N
dp = [[0] * N for _ in range(N)]

h = [-1] * N
idx = 0
e = [0] * M
ne = [0] * M
w = [0] * M


def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def dfs(u, father):
    global h,dp,ne,w,e
    x = h[u]
    while x != 0:
        #print('chulai')
        son = e[x]
        if son == father:
            x = ne[x]
            continue
        dfs(son, u)
        for j in range(m, -1, -1):
            for k in range(j):
                dp[u][j] = max(dp[u][j], dp[u][j - k - 1] + dp[son][k] + w[x])
        x = ne[x]


n, m = map(int, input().split())
for i in range(n - 1):
    a, b, c = map(int, input().split())
    add(a, b, c)
    add(b, a, c)
dfs(1, -1)
print(dp[1][m])
'''

N = 110
M = N * 2
f = [[0] * N for _ in range(N)]
v = [0] * N
up = [[0] * N for _ in range(N)]  # 存储下标对应子节点
sub = [0] * N  # 存储子节点个数
father=[0]*N
n, m = map(int, input().split())
for i in range(1,n):
    a, b, c = map(int, input().split())

    if father[b]!=0:
        father[a]=b # b是a的父节点
        up[b][sub[b]]=a
        sub[b]+=1
        v[a]=c
    else:
        father[b]=a # a是b的父节点
        up[a][sub[a]]=b
        sub[a]+=1
        v[b]=c
def dfs(u):
    for i in range(sub[u]):
        s=up[u][i]
        dfs(s)
        for j in range(m,-1,-1):
            for k in range(j):
                f[u][j]=max(f[u][j],f[u][j-k-1]+f[s][k]+v[s])

dfs(1)
print(f[1][m])