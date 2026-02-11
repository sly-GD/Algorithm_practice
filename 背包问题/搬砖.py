# iridescent_sly time:18:04 date:2024/5/15
n = int(input())


class node():
    def __init__(self, x, y):
        self.weight = x
        self.value = y


a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(node(x, y))
    # print(a[i].weight,a[i].value)

a.sort(key=lambda x: x.value + x.weight)  # 贪心的排序方式

# for i in range(n):
#     print(a[i].weight, a[i].value)

dp = [[0] * 20050 for i in range(n+1)]
ans = 0
for i in range(1, n + 1):
    for j in range(1,20050):
        dp[i][j]=dp[i-1][j]
    for j in range(a[i-1].weight,a[i-1].weight + a[i-1].value + 1):
        dp[i][j] = max(dp[i][j], dp[i-1][j - a[i-1].weight] + a[i-1].value)
        ans = max(dp[i][j], ans)
print(ans)
