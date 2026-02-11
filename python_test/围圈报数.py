n=int(input())
a=list(map(int,input().split())) #eval(字符串) 可以将字符串转换成元组
c=0 #指针
val=0
for i in a:
    c+=1
    val+=1
    if c>n:
        c=1
    if (val%3==0 or '3' in str(val)) and i!=0:  #没报过
        print('cuo')
        print(c)
        break
    if (val%3!=0 or '3' not in str(val)) and i!=val:  #报错数
        print('cu')
        print(c)
        break
 
