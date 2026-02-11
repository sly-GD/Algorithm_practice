s=input()
b=''


for i in range(len(s)):
    if '0'<=s[i]<='9':
        b=b+s[i]
    else:
        b=b+' '
b=b.split()
print(b)
c=[]
for i in b:
    c.append(len(i))
print(max(c))
