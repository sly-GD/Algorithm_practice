# iridescent_sly time:21:14 date:2024/5/27
N = int(2e5) + 10
"""无向图O（Elog E）适用于边少的图，稀疏图"""
p = [0] * N
e=[]  # 边集

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

n=10
m=10
u=1
v=1
w=1
ans=0
cnt=0
'''
n:点数
m:边数
u、v：边的两端节点
cnt：表示已经加入最小生成树的边的个数
ans：最终生成树的权值
'''
#n,m=map(int,input().split())

for _ in range(m):
    u,v,w=map(int,input().split())
    e.append(Edge(u,v,w))

e.sort(key=lambda x: x.w)

'''初始化并查集'''
for _ in range(1,n+1):
    p[_]=_

'''枚举每一条边'''
for i in range(m):
    u=e[i].u;v=e[i].v;w=e[i].w
    u=find(u);v=find(v)  # 分别查找u、v的祖宗节点
    if u!=v:  # u和v不在一个集合
        p[u]=v  # 合并集合
        ans+=w
        cnt+=1 # cnt最多为n-1

if cnt<n-1:
    print("无法生成")
else:
    print("最小生成树权值=",ans)

