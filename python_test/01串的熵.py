import os
import sys
import math
# 请在此输入您的代码
x=23333333

for i in range(10000000,x//2):
    j=x-i
    if i%1000000==0:
        print(i)
    if round(-(j/x)*(math.log2(j/x))*j - (i/x)*(math.log2(i/x))*i,4)==11625907.5798:
        print(i)
