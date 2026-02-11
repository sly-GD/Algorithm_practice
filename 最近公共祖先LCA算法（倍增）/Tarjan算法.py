# iridescent_sly time:16:41 date:2024/5/29
N=int(1e5)

e=[[]*N for i in range(N)]
query=[[]*N for i in range(N)]
fa=[0]*N
vis=[False]*N
ans=[0]*N
#print(query)
n,m,s=map(int,input().split())
for i in range(1,n):
    x,y=map(int,input().split())
    e[x].append(y)
    e[y].append(x)
    '''双向加边'''

for i in range(1,m+1):
    x,y=map(int,input().split())
    query[x].append((y,i))
    query[y].append((x,i))
    '''存储查询'''
# for i in range(10):
#
#     print(query[i][:10])
for i in range(N):
    fa[i]=i
    '''初始化并查集的fa数组'''

def find(x):
    if fa[x]==x:
        return x
    fa[x]=find(fa[x])
    return fa[x]
'''带压缩路径的查找函数'''

def tarjan(u):
    vis[u]=True  # 打标记
    for i in e[u]:
        if not vis[i]:
            tarjan(i) #递归深搜
            fa[i]=u  # 回溯时维护fa数组
    '''遍历该点的查询'''
    for q in query[u]:
        #print(q[0])
        v=q[0]
        i=q[1]
        if vis[v]:
            ans[i]=find(v)


tarjan(s)
# print(ans[:20])

for i in range(len(ans)):
    if ans[i]:
        print(ans[i])

