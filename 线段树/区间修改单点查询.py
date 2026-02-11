# iridescent_sly time:20:35 date:2024/5/21
n, x = map(int, input().split())
N = int(1e6) + 10
t = [0] * (4 * N)
a = [0] + list(map(int, input().split()))



'''做区间修改时只需要存储叶子节点就可以 ， 修改时只修改目标区间的分支节点 '''
'''做单点查询，任何区间内的点从上到下寻找，都会经过修改节点增加的k值。'''
'''从上到叶加和即可'''
'''所以建树函数，和修改函数均不需要push_up函数'''
def treeBulid(q, l, r):
    if l == r:
        t[q] = a[l]
        return
    mid = (l + r) >> 1
    treeBulid(q * 2, l, mid)
    treeBulid(q * 2 + 1, mid + 1, r)

    #t[q] = t[q * 2] + t[q * 2 + 1]


treeBulid(1, 1, n)


def modify(ql,qr, k, q, l, r):
    if  ql<= l and qr >= r:
        t[q]+=k
        '''l,r 包含在 ql,qr 中'''
        return
    mid = (l + r) >> 1
    if ql <= mid:
        modify(ql,qr, k, q * 2, l, mid)
    if qr > mid:
        modify(ql,qr, k, q * 2 + 1, mid + 1, r)
    #t[q] = t[q * 2] + t[q * 2 + 1]


def query(x, q, l, r):
    ans=0
    ans+=t[q]
    if l==r:
        return ans
    mid = (l + r) >> 1
    if x <= mid:
        ans += query(x, q * 2, l, mid)
    if x > mid:
        ans += query(x, q * 2 + 1, mid + 1, r)
    return ans


# modify(1, 5, 1, 1, n)
for _ in range(x):
    u = list(map(int, input().split()))
    if u[0] == 1:
        modify(u[1], u[2],u[3], 1, 1, n)
    if u[0] == 2:
        print(query(u[1], 1, 1, n))
    u.clear()