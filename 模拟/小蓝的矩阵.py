# iridescent_sly time:14:37 date:2024/5/8
N = 205
n = int(input())
s = [["" for _ in range(N)] for _ in range(N)]
t = [["" for _ in range(N)] for _ in range(N)]
m2 = [["" for _ in range(N)] for _ in range(N)]
m3 = [["" for _ in range(N)] for _ in range(N)]
m4 = [["" for _ in range(N)] for _ in range(N)]
vt = []

for i in range(1, n + 1):
    s[i][1:] = input()
for i in range(1, n + 1):
    t[i][1:] = input()
    for j in range(1, n + 1):
        if t[i][j] == '#':
            vt.append((i, j))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        m2[j][n - i + 1] = s[i][j]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        m4[j][n - i + 1] = m2[i][j]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        m3[j][n - i + 1] = m4[i][j]


def check(a):
    global vt
    va = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i][j] == '#':
                va.append((i, j))
    if len(va) != len(vt):
        return False
    else:
        '''计算坐标偏移量'''
        mx=va[0][0]-vt[0][0]
        my=va[0][1]-vt[0][1]
        for i in range(len(va)):
            if va[i][0]-vt[i][0]!=mx or va[i][1]-vt[i][1]!=my:
                return False
        return True
if check(s) or check(m2) or check(m3) or check(m4):
    print("Yes")
else:
    print("No")