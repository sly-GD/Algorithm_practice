'''n=int(input())
s=k=0
for i in range(n):
    x=int(input())
    k+=1
    s+=x
    if k==n:
        break

##print('{:.2f}'.format(s/k))
'''

list1=list(map(int,input().rsplit()))
n=list1[0]
list1.pop(0)
while n>len(list1):
    list1.extend(map(int,input().rsplit()))
print("%.2f"%(sum(list1)/n))
