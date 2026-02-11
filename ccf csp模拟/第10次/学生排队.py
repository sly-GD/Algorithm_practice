# iridescent_sly time:20:03 date:2024/6/1
n=int(input())
m=int(input())
a=list(range(1,n+1))

for i in range(m):
    u,v=map(int,input().split())
    x=a.index(u)
    a.remove(u)
    a.insert(x+v,u)
print(*a)