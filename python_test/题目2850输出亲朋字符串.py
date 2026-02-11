a=input()
b=[]
for i in range(len(a)-1):
    b.append(chr(ord(a[i])+ord(a[i+1])))
b.append(chr(ord(a[-1])+ord(a[0])))
#for i in b:
#    print(i,end='')
c=''.join(b)
print(c)
