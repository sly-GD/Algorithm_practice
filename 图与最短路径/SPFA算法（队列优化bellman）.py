# iridescent_sly time:11:43 date:2024/5/30
from collections import deque


class edge:
    def __init__(self,v,w):
        self.v=v
        self.w=w
N=int(1e5)
e=[[]*N for _ in range(N)]
# e=[[]*N for _ in range(N)]
vis=[False]*N
cnt=[0]*N
d=[float('inf')]*N
q=deque()

n, m, s = map(int, input().split())

for _ in range(m):
    a, b, w = map(int, input().split())
    e[a].append(edge(b,w))


def SPFA(root):
    d[root]=0
    vis[root]=True
    q.append(root)
    while q:
        u=q.popleft()
        vis[u]=False  # 出队就要去除标记，可能再次入队
        for i in e[u]:
            v=i.v
            w=i.w
            if d[v]>d[u]+w:
                d[v]=d[u]+w
                cnt[v]=cnt[u]+1
                if cnt[v]>=n:# 因为最短路 最多n-1条边。大于等于n 说明出现了环
                    return True
                if not vis[v]:
                    q.append(v)
                    vis[v]=True

    return False
SPFA(s)


for i in range(1,n+1):
    if d[i]==float('inf'):
        print(2**31-1,end=' ')
    else:
        print(d[i],end=' ')