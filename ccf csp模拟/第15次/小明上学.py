# iridescent_sly time:19:25 date:2024/5/29
r, y, g = map(int, input().split())

n = int(input())
res = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == 0 or a == 1:
        res += b
    elif a == 2:
        res += b + r
    else:
        pass

print(res)