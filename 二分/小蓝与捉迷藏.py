# iridescent_sly time:14:30 date:2024/5/3
n = int(input())
a = list(map(int, input().split()))
a.sort()


def check(x):
    if x < max(a):
        return False
    t = 0
    for i in a:
        if i > x:
            return False
        else:
            t += x - i
    return t >= x


l = 0
r = int(1e45)
ans = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)
