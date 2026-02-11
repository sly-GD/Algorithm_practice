# iridescent_sly time:15:51 date:2024/5/5
n = int(input())

a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    if x<=y:
        a.append((x,y))
    else:
        b.append((x,y))
a.sort(key=lambda x: x[0])
b.sort(key=lambda x: x[1],reverse=True)


space=0
ans=0
for i in a:
    if space<i[0]:
        te=i[0]-space
        ans+=te
        space+=te
    space+=i[1]-i[0]
for i in b:
    if space<i[0]:
        te=i[0]-space
        ans+=te
        space+=te
    space-=i[0]-i[1]
print(ans)