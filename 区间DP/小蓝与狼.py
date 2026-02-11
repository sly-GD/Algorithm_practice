# iridescent_sly time:17:44 date:2024/5/20
import sys

inf = sys.maxsize
N = 10100
s = [0] * N
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    s[i] = a[i - 1]
    s[n + i] = s[i]
s[2 * n + 1] = a[0]
f = [[inf] * N for _ in range(N)]
for i in range(1,n<<1+1):
    f[i][i]=f[i][i+1]=0

ans=inf
if n == 1:
    print(1)
else:
    for le in range(2, n+1):
        for l in range(1, 2 * n  -le + 2):
            r = l + le-1
            # if r>(n<<2):
            #     continue
            for k in range(l+1,r):
                f[l][r]=min(f[l][r],f[l][k]+f[k][r]+s[l]+s[r])


    '''最后两只狼只加一边'''
    '''循环枚举两只狼，加其两边，取小'''
    for x in range(1,n+1):
        for y in range(x+1,n+1):
            ans=min(ans,f[x][y]+f[y][x+n]+min(s[x],s[y]))
    print(ans+n)