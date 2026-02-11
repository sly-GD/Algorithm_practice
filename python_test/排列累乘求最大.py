'''1 2 3 5 6 8 9 6

123 235 356 568 689 896
'''
'''
a=list(map(int,input().split()))
a.sort()
a[-1],a[len(a)//2],a[1]=a[1],a[-1],a[len(a)//2]
if len(a)>4:
    a[-2],a[3]=a[3],a[-2]
s=0
print(a)
for i in range(2,len(a)):
   s+=a[i-2]*a[i-1]*a[i]
print(s)

'''


#全排列
a=[1,2,3,4]
n=len(a)

f=[0]*(n)  # 每一位可取数的标记
b=[0]*(n)  # 记录每一次结果
maxp=0
def nums(i):  #i为递归的层次
    global maxp
    if i==n:
        #print(b)
        temp=0
        for j in range(n-2):
            temp+=b[j]*b[j+1]*b[j+2]
        maxp=max(temp,maxp)
        #print(temp,maxp)
        return
    for x in range(n):
        if f[x]==0:
            f[x]=1
            b[i]=a[x]
            nums(i+1)
            f[x]=0



nums(0)  #从第一个开始
print(maxp)
