# # iridescent_sly time:20:18 date:2024/5/18
# n, m = map(int, input().split())
# fu = [0, 1] + list(map(int, input().split()))
# w = [0] + list(map(int, input().split()))
# N = 5 * int(1e5)
# a = [[0] * (n + 1) for _ in range(N)]
#
# b = [0] * (n + 1)
# for i in range(2, len(fu)):
#     a[fu[i]][b[fu[i]]] = i
#     b[fu[i]] += 1
#
#
#
#
# #
# #
# # def fun1(u, v):
# #     for i in range(b[u]):
# #         son = a[u][i]
# #         if v == 0:
# #             fun1(son, 1)
# #             a[u].remove(son)
# #             b[u] -= 1
# #             w[u] += w[son]
# #             w[son] = 0
# #         a[fu[u]][b[fu[i]]] = son
# #         b[fu[i]] += 1
# #
# #
# #
# #
# # def fun2(u, v):
# #     '''print()
# #     for i in range(n):
# #         print(a[i][:10])
# #     print('b',b)
# #     print()
# #     '''
# #     if u == 1:
# #         print(1)
# #         return
# #     for i in range(b[1]):
# #         son = a[u][i]
# #         if son == u:
# #             print(v)
# #             return
# #         fun2(son, v + 1)
# #
# #
# # for i in range(m):
# #     x, y = map(int, input().split())
# #     print('第{}'.format(i),x,y)
# #     if x == 1:
# #         fun1(y, 0)
# #         print(b[y], w[y])
# #     if x==2:
# #         fun2(y, 1)





# Created by Pujx on 2024/5/8.

import sys
import math
from collections import defaultdict, deque
from functools import lru_cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from operator import itemgetter
from typing import List, Tuple, Dict, Any

sys.setrecursionlimit(1000000)
input = sys.stdin.read
inf = float('inf')
mod = 998244353

def yn(x):
    print("yes" if x else "no")

def Yn(x):
    print("Yes" if x else "No")

def YN(x):
    print("YES" if x else "NO")

def mem(x, i):
    for j in range(len(x)):
        x[j] = i

def cinarr(a, n):
    for i in range(1, n + 1):
        a[i] = int(input().strip())

def cinstl(a):
    for i in range(len(a)):
        a[i] = int(input().strip())

def coutarr(a, n):
    for i in range(1, n + 1):
        print(a[i], end=" \n"[i == n])

def coutstl(a):
    print(' '.join(map(str, a)))

def all(x):
    return x

def md(x):
    return (x % mod + mod) % mod

N = int(5e5 + 5)
mod = 998244353

a = [0] * N
n, m, t, k, q = 0, 0, 0, 0, 0

fa = [0] * N
head = [0] * N
tail = [0] * N
sz = [0] * N
to = [0] * N
nxt = [0] * N
cnt = 0
d = [0] * N

def add(u, v):
    global cnt
    cnt += 1
    if not sz[u]:
        tail[u] = cnt
    to[cnt] = v
    nxt[cnt] = head[u]
    head[u] = cnt
    sz[u] += 1

def merge(u, v):
    if not sz[v]:
        return
    if not sz[u]:
        head[u] = head[v]
    else:
        nxt[tail[u]] = head[v]
    tail[u] = tail[v]
    sz[u] += sz[v]

dep = [0] * N
l = [0] * N
r = [0] * N
tot = 0
dfn = []

def dfs(u):
    global tot
    l[u] = tot = tot + 1
    dfn.append(u)
    i = head[u]
    while i:
        v = to[i]
        dep[v] = dep[u] + 1
        dfs(v)
        i = nxt[i]
    r[u] = tot

class SegmentTree:
    class TreeNode:
        def __init__(self):
            self.l = 0
            self.r = 0
            self.add = 0
            self.st = -inf
            self.sum = 0
            self.mx = -inf
            self.mn = inf

    def __init__(self):
        self.tr = [self.TreeNode() for _ in range(N << 2)]

    def pushup(self, s):
        self.tr[s].sum = self.tr[s << 1].sum + self.tr[s << 1 | 1].sum
        self.tr[s].mx = max(self.tr[s << 1].mx, self.tr[s << 1 | 1].mx)
        self.tr[s].mn = min(self.tr[s << 1].mn, self.tr[s << 1 | 1].mn)

    def pushdown(self, s):
        if self.tr[s].st != -inf:
            self.tr[s].st += self.tr[s].add
            self.tr[s << 1].add = self.tr[s << 1 | 1].add = 0
            self.tr[s << 1].st = self.tr[s << 1 | 1].st = self.tr[s].st
            self.tr[s << 1].sum = self.tr[s].st * (self.tr[s << 1].r - self.tr[s << 1].l + 1)
            self.tr[s << 1 | 1].sum = self.tr[s].st * (self.tr[s << 1 | 1].r - self.tr[s << 1 | 1].l + 1)
            self.tr[s << 1].mx = self.tr[s << 1 | 1].mx = self.tr[s].st
            self.tr[s << 1].mn = self.tr[s << 1 | 1].mn = self.tr[s].st
            self.tr[s].st = -inf
            self.tr[s].add = 0
        elif self.tr[s].add:
            self.tr[s << 1].add += self.tr[s].add
            self.tr[s << 1 | 1].add += self.tr[s].add
            self.tr[s << 1].sum += self.tr[s].add * (self.tr[s << 1].r - self.tr[s << 1].l + 1)
            self.tr[s << 1 | 1].sum += self.tr[s].add * (self.tr[s << 1 | 1].r - self.tr[s << 1 | 1].l + 1)
            self.tr[s << 1].mx += self.tr[s].add
            self.tr[s << 1 | 1].mx += self.tr[s].add
            self.tr[s << 1].mn += self.tr[s].add
            self.tr[s << 1 | 1].mn += self.tr[s].add
            self.tr[s].add = 0

    def build(self, l, r, s=1):
        self.tr[s].l = l
        self.tr[s].r = r
        self.tr[s].add = 0
        self.tr[s].st = -inf
        self.tr[s].sum = 0
        self.tr[s].mx = -inf
        self.tr[s].mn = inf
        if l == r:
            self.tr[s].sum = self.tr[s].mx = self.tr[s].mn = dep[dfn[l - 1]]
            return
        mid = (l + r) >> 1
        if l <= mid:
            self.build(l, mid, s << 1)
        if mid < r:
            self.build(mid + 1, r, s << 1 | 1)
        self.pushup(s)

    def update(self, l, r, val, s=1):
        if l <= self.tr[s].l and self.tr[s].r <= r:
            self.tr[s].add += val
            self.tr[s].sum += val * (self.tr[s].r - self.tr[s].l + 1)
            self.tr[s].mx += val
            self.tr[s].mn += val
            return
        self.pushdown(s)
        mid = (self.tr[s].l + self.tr[s].r) >> 1
        if l <= mid:
            self.update(l, r, val, s << 1)
        if mid < r:
            self.update(l, r, val, s << 1 | 1)
        self.pushup(s)

    def modify(self, l, r, val, s=1):
        if l <= self.tr[s].l and self.tr[s].r <= r:
            self.tr[s].add = 0
            self.tr[s].st = val
            self.tr[s].sum = val * (self.tr[s].r - self.tr[s].l + 1)
            self.tr[s].mx = self.tr[s].mn = val
            return
        self.pushdown(s)
        mid = (self.tr[s].l + self.tr[s].r) >> 1
        if l <= mid:
            self.modify(l, r, val, s << 1)
        if mid < r:
            self.modify(l, r, val, s << 1 | 1)
        self.pushup(s)

    def query(self, l, r, s=1):
        if l <= self.tr[s].l and self.tr[s].r <= r:
            return self.tr[s].sum
        mid = (self.tr[s].l + self.tr[s].r) >> 1
        ans = 0
        self.pushdown(s)
        if l <= mid:
            ans += self.query(l, r, s << 1)
        if mid < r:
            ans += self.query(l, r, s << 1 | 1)
        return ans

    def queryMax(self, l, r, s=1):
        if l <= self.tr[s].l and self.tr[s].r <= r:
            return self.tr[s].mx
        mid = (self.tr[s].l + self.tr[s].r) >> 1
        ans = -inf
        self.pushdown(s)
        if l <= mid:
            ans = max(ans, self.queryMax(l, r, s << 1))
        if mid < r:
            ans = max(ans, self.queryMax(l, r, s << 1 | 1))
        return ans

    def queryMin(self, l, r, s=1):
        if l <= self.tr[s].l and self.tr[s].r <= r:
            return self.tr[s].mn
        mid = (self.tr[s].l + self.tr[s].r) >> 1
        ans = inf
        self.pushdown(s)
        if l <= mid:
            ans = min(ans, self.queryMin(l, r, s << 1))
        if mid < r:
            ans = min(ans, self.queryMin(l, r, s << 1 | 1))
        return ans

T = SegmentTree()

def work():
    global n, m
    n, m = map(int, input().split())
    for i in range(2, n + 1):
        fa[i] = int(input().strip())
        add(fa[i], i)
    cinarr(d, n)
    dfs(1)
    T.build(1, n)

    for _ in range(m):
        op, u = map(int, input().split())
        if op == 1:
            tmp = head[u]
            head[u] = tail[u] = sz[u] = 0
            i = tmp
            while i:
                v = to[i]
                d[u] += d[v]
                merge(u, v)
                i = nxt[i]
            print(sz[u], d[u])
            if l[u] + 1 <= r[u]:
                T.update(l[u] + 1, r[u], -1)
        else:
            print(T.query(l[u], l[u]) + 1)

if __name__ == "__main__":
    work()


