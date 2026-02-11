n=int(input())        #将数字“8”“6”组合转换为01排列
                    #   并利用2**方减去计算偏移量
s=0
i=0
while s<n:
    s+=2**(i+1)
    i+=1

offset= n-(s-(2**i))-1  #偏移量

a=bin(offset)[2:]
res='0'*(i-len(a))+a


print(res.replace('0','6').replace('1','8'))    #替换01串



offset= n-s-(2**i)-1 
