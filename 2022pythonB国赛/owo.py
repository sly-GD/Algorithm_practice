# iridescent_sly time:17:19 date:2024/5/30
import os
import sys

# 请在此输入您的代码
n=int(input())
s=''
p=[]
for i in range(n):
    a=input()
    #print(s)
    if i!=0:
        if a[0]==p[0][-1]:
            s=p[1]
        else:
            s=p[0]
    # print(s)
    s1=s+a
    s2=a+s
    cnt1=0
    cnt2=0
    x=-1
    flag=1
    while x!=-1 or flag==1:
        flag=0
        x=s1.find('owo',x+1)
        if x!=-1:
            cnt1+=1
    x=-1
    flag=1
    while x!=-1 or flag==1:
        flag=0
        x=s2.find('owo',x+1)
        if x!=-1:
            cnt2+=1
    if cnt1>cnt2:
        print(cnt1)
        s=s1
    elif cnt2>cnt1:
        print(cnt2)
        s=s2
    else:
        print(cnt1)
        p=[s1,s2]