from typing import List
import sys


class Line:
    def __init__(self, x1, x2, y, tag):
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.tag = tag

    def __lt__(self, other):
        return self.y < other.y


class SegmentTree:
    def __init__(self, n):
        self.tree = [None] * (4 * n)
        self.X = []

    def build(self, u, l, r):
        self.tree[u] = {'l': l, 'r': r, 'cnt': 0, 'len': 0}
        if l == r:
            return
        mid = (l + r) // 2
        self.build(2 * u, l, mid)
        self.build(2 * u + 1, mid + 1, r)

    def pushup(self, u):
        if self.tree[u]['cnt']:
            self.tree[u]['len'] = self.X[self.tree[u]['r'] + 1] - self.X[self.tree[u]['l']]
        else:
            self.tree[u]['len'] = self.tree[2 * u]['len'] + self.tree[2 * u + 1]['len']

    def change(self, u, l, r, tag):
        if l > self.tree[u]['r'] or r < self.tree[u]['l']:
            return
        if l <= self.tree[u]['l'] and self.tree[u]['r'] <= r:
            self.tree[u]['cnt'] += tag
            self.pushup(u)
            return
        self.change(2 * u, l, r, tag)
        self.change(2 * u + 1, l, r, tag)
        self.pushup(u)


def unique_and_sorted(lst):
    return sorted(set(lst))


def lower_bound(lst, x):
    lo = 0
    hi = len(lst) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo if lst[lo] == x else lo + 1


def main():
    n = int(sys.stdin.readline().strip())
    lines = []
    X = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
        lines.append(Line(x1, x2, y1, 1))
        lines.append(Line(x1, x2, y2, -1))
        X.extend([x1, x2])
    lines.sort()
    X = unique_and_sorted(X)
    s = len(X)

    seg_tree = SegmentTree(s)
    seg_tree.build(1, 0, s - 2)  # 区间从0开始  

    ans = 0
    for i in range(len(lines) - 1):
        l = lower_bound(X, lines[i].x1)
        r = lower_bound(X, lines[i].x2) - 1  # 注意这里要减1，因为区间是左闭右开的  
        seg_tree.change(1, l, r, lines[i].tag)
        ans += seg_tree.tree[1]['len'] * (lines[i + 1].y - lines[i].y)

    print(ans)


if __name__ == "__main__":
    main()