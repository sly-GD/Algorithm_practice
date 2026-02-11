# iridescent_sly time:11:16 date:2024/5/7
import math

a, b, n = map(int, input().split())


'''快速幂算法'''
def BinExp(a, n):
    r = 1
    while n != 0:
        '''n%2 可以==> n&1 与运算'''
        if n % 2 == 1:
            r = r * a
        a = a * a
        '''对n除2向下取整==> n>>1'''
        n = math.floor(n / 2)
    return r

def ksm(a,n,b):
    r=1
    while n!=0:
        if n&1==1:
            r=r*a%b
        a*=a
        n>>=1
    return r
#print(ksm(10,n-1,b))
t=a*ksm(10,n-1,b) % b
'''得到的t是除n-1次得到的下面的那个余数，要计算后面的商还要接着*10运算下去'''
for i in range(3):
    print(int(10*t/b),end="")
    t=int(t*10%b)
#print(t)