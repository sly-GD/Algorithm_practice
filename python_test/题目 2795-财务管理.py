n=0
list1=[]
while n<12:
    list1.extend(map(float,input().rsplit()))
    n+=1
print("$%.2f"%(sum(list1)/n))
