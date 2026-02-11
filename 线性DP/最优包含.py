# iridescent_sly time:11:39 date:2024/5/13
a = list(input())
b = list(input())
N = 1010
dp = [[float('inf')] * N for i in range(N)]
for i in range(len(a) + 1):
    dp[i][0] = 0  # j等于0时不用改，要赋0后面都取最小
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + 1)
print(dp[len(a)][len(b)])
