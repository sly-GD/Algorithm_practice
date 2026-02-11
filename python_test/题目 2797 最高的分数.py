list1=list(map(int,input().rsplit()))
n=list1[0]
list1.pop(0)
list1.extend(map(int,input().rsplit()))
print(max(list1))
