list1=list(map(int,input().rsplit()))
n=list1[0]
list1.pop(0)
while n>len(list1):
    list1.extend(map(int,input().rsplit()))
print(sum(list1),end=" ")
print("%.5f"%(sum(list1)/n))
