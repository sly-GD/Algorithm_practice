# iridescent_sly time:20:35 date:2024/5/21
n, x = map(int, input().split())
N = int(1e6) + 10
t = [0] * (4 * N)
a = [0] + list(map(int, input().split()))


def treeBulid(q, l, r):
    if l == r:
        t[q] = a[l]
        return
    mid = (l + r) >> 1
    treeBulid(q * 2, l, mid)
    treeBulid(q * 2 + 1, mid + 1, r)
    t[q] = t[q * 2] + t[q * 2 + 1]


treeBulid(1, 1, n)


def modify(x, k, q, l, r):
    if l == r:
        t[q] += k
        return
    mid = (l + r) >> 1
    if x <= mid:
        modify(x, k, q * 2, l, mid)
    else:
        modify(x, k, q * 2 + 1, mid + 1, r)
    t[q] = t[q * 2] + t[q * 2 + 1]


def query(ql,qr,q,l,r):
    if ql<=l and qr>=r:
        '''l,r 包含在 ql,qr 中'''

        return t[q]
    ans=0
    mid=(l+r)>>1
    if ql<=mid:
        ans+=query(ql,qr,q*2,l,mid)
    if qr>mid:
        ans+= query(ql,qr,q*2+1,mid+1,r)
    return ans

#modify(1, 5, 1, 1, n)
for _ in range(x):
    u,v,w=map(int,input().split())
    if u==1:
        modify(v,w,1,1,n)
    if u==2:
        print(query(v, w, 1, 1, n))