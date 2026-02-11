# iridescent_sly time:17:12 date:2024/5/5
n, m, k = map(int, input().split())
# a=[0]*20010
minb = [0] * 200010
for i in range(1, n + 1):
    minb[i] = m + 1
for i in range(1, k + 1):
    x, y = map(int, input().split())
    # a[i]=(x,y)
    minb[x] = min(minb[x], y)
# print(minb[:10])
border = 1
for i in range(1, n):
    if minb[i + 1] <= border:
        print(i)
        exit()
    if minb[i + 1] > border + 1:
        border += 1
print(n)
"""
N = 200010
x = [0] * N
y = [0] * N
minM = [0] * N

n, m, k = map(int, input().split())

for i in range(1, n + 1):
    minM[i] = m + 1

for i in range(1, k + 1):
    x[i], y[i] = map(int, input().split())
    minM[x[i]] = min(minM[x[i]], y[i])
print(minM[:10])
border = 1
for i in range(1, n):
    if minM[i + 1] <= border:
        print(i)
        exit()
    if minM[i + 1] > border + 1:
        border += 1

"""
