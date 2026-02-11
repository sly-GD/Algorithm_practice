a=input()
flag=False
for i in a:
    if a.count(i)==1:
        print(i)
        flag=True
        break
#if flag==False:
if not flag:
    print("no")
