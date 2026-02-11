# iridescent_sly time:19:43 date:2024/5/30
import sys

n=10**8
a=[False]*(n+10)
sys.stdin = open("D:\学习\算法\洛谷\蓝桥杯\十三届PythonB组国赛\primes.txt", 'r')
'''将文件读取到缓冲区中，下面直接input（）就可以'''

def prime(n):

    a[0]=True
    a[1]=True
    for i in range(2,n+1):
        if a[i]==False:
            for j in range(2*i , n+1,i):
                a[j]=True
prime(n)
cnt=0
for i in range(2000000):
    x=int(input())
    if a[x]==False:
        cnt+=1
print(cnt)