# iridescent_sly time:21:01 date:2024/5/29
n = int(input())
m = int(input())
root = int(input())
N = 5 * int(1e4) + 10
fa=[0]*(n+10)
tcp=0
class edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

for _ in range(len(fa)):
    fa[_]=_
def find(x):
    if x==fa[x]:
        return x
    fa[x]=find(fa[x])
    return fa[x]
e = [edge(0, 0, 0)] + [] * N
#vis = [False] * (n + 10)
bianqu=[]
for _ in range(m):
    a, b, c = map(int, input().split())
    e.append(edge(a,b,c))

e.sort(key=lambda x: x.w)

for i in e:
    u=i.u
    v=i.v
    w=i.w
    u=find(u)
    v=find(v)
    if u!=v:
        tcp+=1
        fa[u]=v
        bianqu.append(w)
    if tcp==n:
        break
print(max(bianqu))