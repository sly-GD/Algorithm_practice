# iridescent_sly time:11:28 date:2024/5/27
n = int(input())


def jiecheng(x, mod):
    res = 0
    w = 1
    for i in range(1, x + 1):
        w = (w * i) % mod
    print(w)


for _ in range(n):
    a, b = map(int, input().split())
    jiecheng(a,b)