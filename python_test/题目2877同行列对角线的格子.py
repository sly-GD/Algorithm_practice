n,r,c=map(int,input().split())
a,b=r,c
#同一行格子
for i in range(n):
    print('(%d,%d)'%(a,i+1),end=' ')
print()
#同一列格子
for i in range(n):
    print('(%d,%d)'%(i+1,b),end=' ')
print()
#主对角线
while True:
    if a==1 or b==1:
        while a<=n and b<=n:
            print('(%d,%d)'%(a,b),end=' ')
            a+=1
            b+=1
        print()
        break
    a-=1
    b-=1
'''
# 主对角线，两个值差相等
for m in range(1, N + 1):
    for n in range(1, N + 1):
        if m - n == i - j:
            print('(%d,%d)' % (m, n), end=' ')
print()
# 副对角线，两个值的和相等
for m in range(N, 0, -1):
    for n in range(1, N + 1):
        if m + n == i + j:
            print('(%d,%d)' % (m, n), end=' ')
'''
#副对角线
a,b=r,c
while True:
    if a==n or b==1:
        while a>=1 and b<=n:
            print('(%d,%d)'%(a,b),end=' ')
            a-=1
            b+=1
        print()
        break
    a+=1
    b-=1
