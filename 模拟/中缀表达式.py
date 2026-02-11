# iridescent_sly time:13:31 date:2024/5/7

N = 10010
n = int(input())

v = [''] * N
l = [0] * N
r = [0] * N
isLeaf = [False] * N
fa = [0] * N
for i in range(1, n + 1):
    v[i], y, z = input().split()
    l[i], r[i] = int(y), int(z)
    if l[i] != -1:
        fa[l[i]] = i
    if r[i] != -1:
        fa[r[i]] = i
    if l[i] == -1 and r[i] == -1:
        isLeaf[i] = True


def dfs(x):
    global l, r, v
    lt, rt = "", ""
    if l[x] != -1:
        lt = dfs(l[x])
        if need(l[x]):
            lt = "(" + lt + ")"
    if r[x] != -1:
        rt = dfs(r[x])
        if need(r[x]):
            rt = "(" + rt + ")"
    return lt + v[x] + rt


def need(x):
    global isLeaf, v, fa, l, r
    if isLeaf[x]:
        return False
    if fa[x] and v[fa[x]] == '-' and l[fa[x]] == -1:
        return True
    if v[x] == "-" and l[x] == -1:
        return True
    if v[x] == '+' or v[x] == '-':
        if fa[x]:
            if r[fa[x]] == x:
                if v[fa[x]] != '+':
                    return True
            else:
                if v[fa[x]] != "+" and v[fa[x]] != '-':
                    return True
    if v[x] == "*" or v[x] == "%" or v[x] == "/":
        if fa[x]:
            if l[fa[x]] == x:
                return False
            else:
                if v[fa[x]] == '/' or v[fa[x]] == '%':
                    return True
    return False


for i in range(1, n + 1):
    if not fa[i]:
        print(dfs(i))
        break
'''
N = 10005
def need(u):
    global isleaf, w, fa, l, r
    if isleaf[u]:
        return False
    if fa[u] and w[fa[u]] == "-" and l[fa[u]] == -1:
        return True
    if w[u] == "-" and l[u] == -1:
        return True
    if w[u] == "-" or w[u] == "+":
        if fa[u]:
            if r[fa[u]] == u:
                if w[fa[u]] != "+":
                    return True
            else:
                if w[fa[u]] != "+" and w[fa[u]] != "-":
                    return True
    if w[u] == "*" or w[u] == "/" or w[u] == "%":
        if fa[u]:
            if l[fa[u]] == u:
                return False
        else:
            if w[fa[u]] == "/" or w[fa[u]] == "%":
                return True
    return False
def dfs(u):
    global w, l, r
    lt, rt = "", ""
    if l[u] != -1:
        lt = dfs(l[u])
        if need(l[u]):
            lt = "(" + lt + ")"
    if r[u] != -1:
        rt = dfs(r[u])
        if need(r[u]):
            rt = "(" + rt + ")"
    return lt + w[u] + rt
if __name__ == "__main__":
    n = int(input())
    w = [""] * N
    l = [0] * N
    r = [0] * N
    fa = [0] * N
    isleaf = [False] * N
    for i in range(1, n + 1):
        w[i], l[i], r[i] = input().split()
        l[i], r[i] = int(l[i]), int(r[i])
        if l[i] != -1:
            fa[l[i]] = i
        if r[i] != -1:
            fa[r[i]] = i
        if l[i] == -1 and r[i] == -1:
            isleaf[i] = True
    for i in range(1, n + 1):
        if not fa[i]:
            print(dfs(i))
            break
'''
