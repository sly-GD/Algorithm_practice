# iridescent_sly time:18:42 date:2024/5/31
N=10050

a=[0]*N
fa=[0]*N
n,m=map(int,input().split())

for i in range(n+1):
    fa[i]=i

def find(x):
    if x!=fa[x]:
        fa[x]=find(fa[x])
    return fa[x]

for _ in range(m):
    u,v,w=map(int,input().split())
    if u==1:
        v=find(v)
        w=find(w)
        if v!=w:
            fa[v]=w
    if u==2:
        if find(v)==find(w):
            print("Y")
        else:
            print("N")