# iridescent_sly time:21:13 date:2024/5/28
n, m = map(int, input().split())
a=[[]*(n+1) for _ in range(n+1)] # 邻接表
N=int(2e5)+50
e=[]
p=[0]*N
class edge:
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w

for _ in range(m):
    x,y,z=map(int,input().split())
    a[x]=y
    a[y]=x
    e.append(edge(x,y,z))

# 利用并查集
def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

e.sort(key=lambda x:x.w)

for i in range(1,n+1):
    p[i]=i
cnt=[]
vis=[0]*(n+1)
for i in range(m):
    u=e[i].u
    v=e[i].v
    w=e[i].w
    x=find(u)
    y=find(v)
    if x!=y:
        vis[u]=1
        vis[v]=1
        p[x]=y
        cnt.append(w)
if 0 in vis[1:]:
    print(-1)
else:
    print(max(cnt))