#a=[0,1,2,3,4,5,6,7,8,9]
num=[]
x=[]
res=0
def dfs(n):
    global res
    if n==10:
        a=num[0]
        b=num[1]
        c=num[2]
        y=num[3]*100+num[4]*10+num[5]
        x=num[6]*100+num[7]*10+num[8]
        if a*c*x+b*x+y*c==10*c*x:
            #print(num)
            res+=1
        return
    for i in range(1,10):
        if i in num:
            continue
        num.append(i)
        #x.append(i)
        dfs(n+1)
        num.remove(i)


dfs(1)
print(res)
