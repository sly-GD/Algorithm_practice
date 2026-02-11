# iridescent_sly time:13:54 date:2024/5/30
import heapq

n, m, s = map(int, input().split())
N = int(1e4)+100
e = [[] * N for _ in range(N)]
vis = [False] * N
d = [float('inf')] * N
q = []


class edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w

for _ in range(m):
    a,b,w=map(int,input().split())
    e[a].append(edge(b,w))
def dijkstra(root):
    d[root] = 0
    heapq.heappush(q, [0, root])
    while q:
        t = heapq.heappop(q)
        u = t[1]
        if vis[u]:
            continue
        vis[u] = True
        for i in e[u]:
            v=i.v
            w=i.w
            if d[v]>d[u]+w:
                d[v]=d[u]+w
                heapq.heappush(q,[d[v],v])

dijkstra(s)

for i in range(1,n+1):
    if d[i]==float('inf'):
        print(2**31-1,end=' ')
    else:
        print(d[i],end=' ')