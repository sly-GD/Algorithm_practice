'''# 引入常用的库
import bisect
# 示例数组
a = [20, 10, 50, 20, 20, 40]
# 对数组进行排序
a.sort() # 10 20 20 20 40 50
# 使用 bisect 模块的 bisect_right 函数寻找右边界
x = 20
index = bisect.bisect_right(a, x)
# 输出位置指针及对应的值
print(index, a[index])
# 输出位置指针
print(index)
# 输出右边界位置
print(bisect.bisect_right(a, x))
# 输出右边界位置
print(bisect.bisect_right(a, 15))
# 输出右边界位置
print(bisect.bisect_right(a, 60))


num=[1,22,2,2,2,3,5,6]

j=0
for i in range(1,len(num)):
    if num[i]!=num[i-1]:
        j+=1
        num[j]=num[i]
print(num)

num=num[:j+1]
print(num)
'''
'''
import os
import sys

# 请在此输入您的代码
n,m=20,20

cnt=m+n-1
num=0
for i in range(1,cnt):
    num+=i
row=cnt
while row>m:
    row-=1
    num+=1
print(num)
'''



n=int(input())
res=0
for i in range(1,n+1):
    x=str(i)
    if '2' in x or '0' in x or '1' in x or '9' in x:
        res+=1 

print(res)




























