n, k = map(int, input().split())

N = 40
f = [[0] * N for _ in range(N)]
'''f[i][j] 表示当前i个节点，高度为j的非对称二叉树的个数'''
f[0][0] = 1
f[1][1] = 1
'''后面是相乘计算，需要设置为1'''

for i in range(2, n + 1):
    for x in range(i):
        y = i - x - 1
        for c in range(x + 1):
            for d in range(y + 1):
                if max(c, d) >= k * min(c, d):
                    f[i][max(c, d) + 1] += f[x][c] * f[y][d]  # 左右子树的每种遍历都要相加
ans = 0
for i in range(len(f[n])):
    ans += f[n][i]
print(ans)
