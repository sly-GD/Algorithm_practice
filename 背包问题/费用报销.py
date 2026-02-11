# iridescent_sly time:17:49 date:2024/5/13
n, m, k = map(int, input().split())


class Ren:
    def __init__(self, m, d, v, t):
        self.m = m
        self.d = d
        self.v = v
        self.t = t


dp = [[0] * 5050 for i in range(1010)]

da = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
s = [0] * 13
for i in range(2, 13):
    s[i] = s[i - 1] + da[i-1]
d = [None] * 1010
for i in range(1, n + 1):
    month, day, value = map(int, input().split())
    time = s[month] + day
    d[i] = Ren(month, day, value, time)
d[0] = Ren(0, 0, 0, 0)
d = [x for x in d if x is not None]
d=sorted(d, key=lambda x: x.t)

last = [0] * 5050
for i in range(1, n + 1):
    for j in range(i):
        if d[i].t - d[j].t >= k:
            last[i] = j

for i in range(1, n + 1):
    for j in range(m, -1, -1):
        dp[i][j] = dp[i - 1][j]
        if j >= d[i].v:
            dp[i][j] = max(dp[i - 1][j], dp[last[i]][j - d[i].v] + d[i].v)
print(dp[n][m])
