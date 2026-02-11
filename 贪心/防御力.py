# iridescent_sly time:14:37 date:2024/5/5
import math

#最终要让d最大
#A和B增加都会影响d的变化
#d=log2A，d=log3B 所以A对d的变化增幅较大
#使用序列是固定的，所以就让B的卡牌优先使用尽量增大D的值，在使用A的较大卡牌
# B优先使用大的，A优先使用小的
#import functools
n1,n2=map(int,input().split())

a=[[i,int(x)] for i,x in enumerate(input().split(),1) ]
b=[[i,int(x)] for i,x in enumerate(input().split(),1) ]
a.sort(key=lambda x: x[1])
b.sort(key=lambda x: x[1],reverse=True)
"""
a=list(map(int,input().split()))
for i in range(n1):
    a[i]=(i,a[i])
b=list(map(int,input().split()))
for i in range(n2):
    b[i]=(i,b[i])

a.sort(key=lambda x: (x[1]))
b.sort(key=lambda x: (x[1]),reverse=True)
#print(a,b)
"""
s=input()
A,B=1,1
d=0
def jisuan(x,m):
   global d,a,b
   if m==1:
       d=math.log(x,2)
   else:
       d=math.log(x,3)

for i in s:
    if i=='0':
        #te=a.pop(0)
        print("A{}".format(a.pop(0)[0]))
        #jisuan(A,1)
    else:
        #te=b.pop(0)
        print("B{}".format(b.pop(0)[0]))
print("E")