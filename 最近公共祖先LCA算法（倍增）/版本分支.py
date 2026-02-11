# iridescent_sly time:17:26 date:2024/5/29
N = int(1e5) + 10

fa = [0] * N
vis = [False] * N
e = [[] * N for _ in range(N)]
query = [[] * N for _ in range(N)]
chaxun = [[0, 0]] + [] * N
ans = [0] * N

n, m = map(int, input().split())
for _ in range(1, n):
    a, b = map(int, input().split())
    e[a].append(b)
    e[b].append(a)

for i in range(1, m + 1):
    a, b = map(int, input().split())
    query[a].append([b, i])
    query[b].append([a, i])
    chaxun.append([a, b])
# print(chaxun[:10])

for i in range(1, n + 1):
    fa[i] = i


def find(x):
    if x == fa[x]:
        return x
    fa[x] = find(fa[x])
    return fa[x]


def tarjan(u):
    global vis, fa, query
    vis[u] = True
    for v in e[u]:
        v=int(v)
        if not vis[v]:
            tarjan(v)
            fa[v] = u

    for q in query[u]:
        j = q[0]
        i = q[1]
        if vis[j]:
            ans[i] = find(j)


tarjan(1)

# print(ans[:10])
for i in range(n + 1):
    if ans[i]:
        if ans[i] == chaxun[i][0]:
            print("YES")
        else:
            print("NO")
