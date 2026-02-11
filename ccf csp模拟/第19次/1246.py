
n=int(input())
s=input()
x='1'
y=''
for i in range(n):
    m=len(x)
    for j in range(m):
        if x[j]=='1':
            y+=str(2**int(x[j]))
            #x=x.replace(x[j],str(2**int(x[j])),1)
            #print(x)
        if x[j] == '2':
            y += str(2 ** int(x[j]))
            #x=x.replace(x[j], str(2 ** int(x[j])),1)
        if x[j] == '4':
            y += str(2 ** int(x[j]))
            #x=x.replace(x[j], str(2 ** int(x[j])),1)
        if x[j] == '6':
            y += str(2 ** int(x[j]))
            #x=x.replace(x[j], str(2 ** int(x[j])),1)
    x=y
    y=''
#print(x)
res=x.count(s)
print(res)