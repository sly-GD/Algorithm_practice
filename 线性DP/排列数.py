# iridescent_sly time:15:07 date:2024/5/13
mod = 123456
N = 505
n, k = map(int, input().split())
dp = [[0] * N for i in range(N)]  # dp[i][j] 表示前i个数有j个折点的排列个数
dp[1][0] = 1  # 1
#dp[2][0] = 2  # 2 1 / 1 2
#dp[3][0] = 2  # 1 2 3 / 3 2 1
for i in range(2, n):
    dp[i][0] = 2
    for j in range(i + 1):
        dp[i + 1][j] += dp[i][j] % mod * (j + 1) % mod
        dp[i + 1][j + 1] += dp[i][j] % mod * 2 % mod
        dp[i + 1][j + 2] += dp[i][j] % mod * (i - j - 2) % mod
print(dp[n][k - 1]%mod)
