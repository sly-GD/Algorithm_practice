# iridescent_sly time:19:36 date:2024/5/10
n, q = map(int, input().split())
mod=int(1e9+7)
a = list(map(int, input().split()))
xo = [0] * (n + 1)


def qpow(x, q):
    if x == 0:
        return 1
    t = qpow(x // 2, q)
    return t * t * (2 if x & 1 else 1)

for i in range(1,n+1):
    a[i-1]=a[i-1]*qpow(a[i-1],mod)
    xo[i]=xo[i-1]^a[i-1]

for i in range(q):
    l,r=map(int,input().split())
    print('No' if xo[r]^xo[l-1] else 'Yes')


'''
l,r=0,0
for i in range(q):
    x = [0] * n
    f=0
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    for j in range(l,r+1):
        x[a[j]]+=1
    #print(x)
    for j in range(l,r):
        if x[j]%2!=0:
            print('No')
            f=1
            break
    if f==0:
        print('Yes')

'''
