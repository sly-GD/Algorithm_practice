'''import datetime
import heapq

a=datetime.date(2014,11,9)
x=datetime.date(2015,1,1)-a
print(x.days)

try:
    print("jinri")
    for y in range(2015+1000):
        for m in range(1,13):
            for d in range(1,32):
                b=datetime.date(y,m,d)
                print(b.date())
                if b-a==1000:
                    print(b.date())
                    
                    
except:
    pass

heap = []
# 插入元素到堆中
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print("堆中的元素:", heap)


a='WHERETHEREISAWILLTHEREISAWAY'
a=list(a)
a.sort()

b=''
for i in a:
    b+=i
print(b)

'''
a=input()
s=set(a)
x={}
for i in s:
    x[i]=0
for i in a:
    x[i]+=1
mx=0
#print(x)
for i in x.values():
    mx=max(i,mx)
res=[]
for j in x:
    #print(j)
    if x[j]==mx:
        res.append(j)  
res.sort()
b=''
for i in res:
    b+=i
print(b) 
