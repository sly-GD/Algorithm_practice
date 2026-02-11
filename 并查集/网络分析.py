# iridescent_sly time:14:24 date:2024/5/26
n, m = map(int, input().split())
N = 10010
fa = [0] * N
d = [0] * N
for _ in range(1, n + 1):
    fa[_] = _


def find(x):
    if fa[x] == x or fa[fa[x]] == fa[x]:
        return fa[x]
    t = find(fa[x])
    d[x] += d[fa[x]]
    fa[x] = t
    return fa[x]


for _ in range(m):
    # print('di{}次'.format(_))
    # print('fa', fa[:15])
    # print('d', d[:15])
    u, v, w = map(int, input().split())
    if u == 1:
        a = find(v)
        b = find(w)
        if a != b:
            #print('zheli',a,b)
            fa[b] = a
            d[b] -= d[a]
    if u == 2:
        a = find(v)
        d[a] += w
# print('fa',fa[:15])
# print('d',d[:15])
for _ in range(1, n + 1):
    if _ == find(_):
        print(d[_], end=" ")
    else:
        print(d[_] + d[find(_)], end=" ")
