# iridescent_sly time:21:44 date:2024/5/21
import math

n, m = map(int, input().split())

a = [0] + list(map(int, input().split()))
N = int(1e5) + 10
tr = [0] * (2 * N)
sum1 = sum(a)

def treeBuild(q, l, r):
    if l == r:
        tr[q] = a[l]
        return
    mid = (l + r) >> 1
    treeBuild(q * 2, l, mid)
    treeBuild(q * 2 + 1, mid + 1, r)
    tr[q] = max(tr[q * 2], tr[q * 2 + 1])


def modify(ql, qr, q, l, r):
    if tr[q] <= 2:
         '''必须要有，会超时'''
         '''小于等于2，作对数无效不用修改'''
         return

    global sum1
    if l == r:
        novel = int(math.log(tr[q], 2) + 1)
        sum1 -= tr[q] - novel
        tr[q] = novel
        return
    mid = (l + r) >> 1
    if ql <= mid:
        modify(ql, qr, q * 2, l, mid)
    if qr > mid:
        modify(ql, qr, q * 2 + 1, mid + 1, r)
    tr[q] = max(tr[q * 2], tr[q * 2 + 1])


treeBuild(1, 1, n)
for _ in range(m):
    x, y = map(int, input().split())
    #print(tr[:10])
    modify(x, y, 1, 1, n)
    print(sum1)
