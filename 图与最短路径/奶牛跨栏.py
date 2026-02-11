# iridescent_sly time:15:23 date:2024/5/22
import sys
N=350

g=[[sys.maxsize]*N for _ in range(N)]

n,m,t=map(int,input().split())

for _ in range(m):
    x,y,z=map(int,input().split())
    g[x][y]=z
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):

            g[i][j]=min(g[i][j],max(g[i][k],g[k][j]))
for _ in range(t):
    x,y=map(int,input().split())
    if g[x][y]!=sys.maxsize:
        print(g[x][y])
    else:
        print(-1)