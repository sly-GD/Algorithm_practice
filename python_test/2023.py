import os
import sys
# 请在此输入您的代码

def findx(x):
    find_1=x.find('2')
    if find_1==-1:
        return 0
    find_2=x.find('0',find_1+1)
    if find_2==-1:
        return 0
    find_3=x.find('2',find_2+1)
    if find_3==-1:
        return 0
    find_4=x.find('3',find_3+1)
    if find_4==-1:
        return 0
        

cnt=0
a=0
for i in range(12345678,98765433):
    if i%1000000==0:
        print(i)
    x=str(i)
    #find(字串，start)寻找字串返回首次出现的索引，如未找到则返回-1
    if findx(x)==0:
        cnt+=1
    '''
  if '2' in x:
    a=x.find('2')
    if '0' in x[a+1:]:
      a=x[a:].index('0')
      if '2' in x[a:]:
        a=x[a:].index('2')
        if '3' in x[a:]:
          cnt+=1'''
print(cnt)
