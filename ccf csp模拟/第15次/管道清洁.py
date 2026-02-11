# iridescent_sly time:21:25 date:2024/5/29
T, S, E = map(int, input().split())
class edge:
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w
N=600
for _ in range(T):
    e=[]*N
    tcp=0
    vis=[[False]*N for _ in range(N)]
    e.append(edge(0,0,0))
    lin=[[]*N for _ in range(N)]
    n,m=map(int,input().split())
    for _ in range(m):
        a,b,c=map(str,input().split())
        e.append(edge(int(a),int(b),c))
        lin[int(a)].append([int(b),c])
    def dfs(x):
        global tcp
        for i in lin[x]:
            if not vis[x][i[0]]:
                vis[x][i[0]]=True
                dfs(i[0])
                tcp+=1

    # else:
    print(len(e)*E)
    # print(lin)