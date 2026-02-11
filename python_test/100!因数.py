ans=1
def zhishu(n):
    for v in range(2,n):
        if n%v==0:
            return False
        else:
            return True
a=[2]
for t in range(2,101):
    if zhishu(t):
        a.append(t)
print(a)

m={}
for i in a:
    m[i]=1

for i in range(2,101):
    for j in a:
        if j>i:
            break
        while i%j==0:
            m[j]+=1
            i//=j
for i in m.values():
    ans*=i
print(ans)
