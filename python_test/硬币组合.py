n = int(input())
nums=list(map(int,input().split(',')))
m=int(input())

def heshu(n):
    for i in range(2,n):
        if n%i==0:
            return True
    return False
res=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            res.append(nums[i]+nums[j]+nums[k])

a=set(res)  #直接把列表转换为集合 可以去重

b=0
for i in a:
    if heshu(i):
        b+=1
a=len(a)
print(f"{a},{b}")
