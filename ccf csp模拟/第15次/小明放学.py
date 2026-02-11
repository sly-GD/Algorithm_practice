# iridescent_sly time:19:25 date:2024/5/29
r, y, g = map(int, input().split())
m = r + g + y


def jud(x):
    x = x % m
    if 0 <= x <= g:
        return 0
    elif x <= r + y:
        return m-x
    else:
        return m-x


n = int(input())
res = 0
ti = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        res += b
    elif a == 1:
        #ti += b
        res += jud(res + r-b+y+g)
    elif a == 2:
        res += jud(res +y-b+g)
    else:
        res += jud(res +g- b )
    #print(i,res)
print(res)
