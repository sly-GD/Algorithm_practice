# iridescent_sly time:19:13 date:2024/5/30
# f=[0]*202202011300
f=[0]*101
'''
由于个位不受进位影响，所以可以利用递推式只计算个位。根据抽屉原理，在100项之内，个位必然出现循环节。
'''
def fun(x):
    if x==1 or x==2:
        return 1
    if  f[x]!=0:
       return f[x]
    return fun(x-1)+fun(x-2)
cnt=0
f[1]=1
f[2]=1
for i in range(3,100):
    x=fun(i)
    f[i]=x%10
    # print(x,end=" ")
    if x%10==7:
        cnt+=1

u=(202202011200//60)
v=202202011200 %60
# print(v)
w=f[:v+1].count(7)
cnt=u*8
# print(f?[61:121])
print(cnt+w)