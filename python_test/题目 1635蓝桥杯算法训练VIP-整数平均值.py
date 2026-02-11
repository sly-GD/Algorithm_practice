n=int(input())
list1=[]
list1=list(map(int,input().rsplit()))
s=0
for i in list1:
    s+=i
print(s//n)
