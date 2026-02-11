# iridescent_sly time:16:15 date:2024/5/6
from collections import deque

n, d = map(int, input().split())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
a.sort(key=lambda x: x[0])
a.insert(0,(0,0))
cl=[False]*(n+1);cr=[False]*(n+1)
q=deque()

for i in range(1,n+1):
    #x,y=a[i][0],a[i][1]
    while q and a[q[-1]][1]<a[i][1]:
        q.pop()
    while q and a[i][0]-a[q[0]][0]>d:
        q.popleft()
    if q and a[q[0]][1]>=a[i][1]*2:
        cl[i]=True
    q.append(i)

q.clear()

for i in range(n,0,-1):
    while q and a[q[-1]][1]<a[i][1]:
        q.pop()
    while q and a[q[0]][0]-a[i][0]>d:
        q.popleft()
    if q and a[q[0]][1]>=a[i][1]*2:
        cr[i]=True
    q.append(i)

ans=sum(cl[i] and cr[i] for i in range(n+1))
print(ans)


