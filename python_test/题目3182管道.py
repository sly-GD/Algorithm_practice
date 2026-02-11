n,ll=map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

def check(ans):# ans为当前时刻
    res=[] # 存放流水区间
    for i in range(n): # 依次计算当前时刻已经有水的区间
        if a[i][1]>ans :
            continue  #把没到时刻的阀门跳过
        l=max(1,a[i][0]-(ans-a[i][1]))# 避免超出管道，所以和1去最大值
        r=min(ll,a[i][0]+(ans-a[i][1]))
        res.append((l,r))
    res.sort() #只会对每个索引值的第一个值进行排序

    if res[0][0]>1 :return False  #s说明第一格没有水
    rr=res[0][1]
    for i in range(1,len(res)):
        if res[i][0]>rr and res[i][0]!=rr+1:
            return False
        else:
            rr=max(rr,res[i][1]) #防止rr已经把第i个阀门包括进去了
    if rr<ll:# 最终也没到达右端
        return False
    return True


#l,r为时间轴两端
l,r=1,2*10**9+1 #最坏的情况只开一个阀门并且在一端
while l+1!=r:
    mid = (l+r)//2
    if check(mid):
        r=mid
    else :
        l=mid
print(r)#结果在最右端





'''n,ln=map(int,input().split())

tube=[0 for i in range(ln)]
a=[[0,0]for i in range(n)]
for i in range(n):
    a[i][0],a[i][1]=map(int,input().split())
res=0
def ceshi():
    if tube.count(0)==0:
        return True    
    return False
while True:
    res+=1
    #print(res)
    while res!=1:
        try:
            z=tube.index(res-1)
        except:
            break
        else:
            tube[z]=100000
            if 0<=z-1<ln and tube[z-1]==0:
                tube[z-1]=res
            if 0<=z+1<ln and tube[z+1]==0:
                tube[z+1]=res
    #print(tube)
    for i in range(n):
        if res==a[i][1]:
            tube[a[i][0]-1]=res
            #print(a[i])
    if ceshi():
        #print("end")
        break
print(res)
'''
