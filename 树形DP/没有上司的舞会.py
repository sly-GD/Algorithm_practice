# iridescent_sly time:17:53 date:2024/5/16
n = int(input())

fa = [False] * (n + 1)  # 存储该节点是否具有父节点 ,用于寻找根节点
a = [[0] * (n + 2) for i in range(n + 1)]  # 存储子节点
b = [0] * (n + 1)  # 存储该节点的子节点个数
w = [0] + [0] * (n + 1)  # 存储快乐指数

dp = [[0] * 2 for _ in range(n + 1)]  # dp[i][0] 表示不取该节点 dp[i][1] 表示取该节点
for i in range(1, n + 1):
    w[i] = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    a[y][b[y]] = x
    b[y] += 1
    fa[x] = True


def dfs(u):
    dp[u][1] = w[u]
    for i in range(b[u]):
        son = a[u][i]
        dfs(son)
        dp[u][0] += max(dp[son][0], dp[son][1])
        dp[u][1] += dp[son][0]


root = 1
while fa[root]:
    root += 1
# print(root)
dfs(root)
print(max(dp[root][0], dp[root][1]))
