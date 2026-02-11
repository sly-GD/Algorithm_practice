n=int(input())
arr=list(map(int,input().split()))
list1=[0]*4
#print(list1[0])
#list1[0]+=1
#print(list1[0])
for i in arr:
    if i<=18:
        list1[0]+=1
    elif i<=35:
        list1[1]+=1
    elif i<=60:
        list1[2]+=1
    else:
        list1[3]+=1
for i in list1:
    print("%.2f%%"%(i/n*100))
