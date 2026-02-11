# iridescent_sly time:19:05 date:2024/5/30
import os
import sys

# 请在此输入您的代码
s=' '+input()
n=int(input())
for i in range(n):
    a,b,c,d=map(str,input().split())
    a=int(a)
    b=int(b)
    s1=s[:a]
    s2=s[b+1:]
    s3=s[a:b+1].replace(c,d)
    s=s1+s3+s2
print(s[1:])
#
# s='abfdfdggggjk'
# print(s[7:].replace('g', 'p'))
# print(s[:1])