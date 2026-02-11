k=int(input())

a,c1,c2=map(str,input().split())

ans=0
cnt=0
'''
f=a.find(c1)
if f==-1:
    print(0)

for i in range(len(a)):
    if a[i]==c1 and i+k-1<len(a):
       for j in range(i+k-1,len(a)):
            if a[j]==c2:
                ans+=1
'''


for i in range(len(a)-k,-1,-1):
    if a[i+k-1]==c2:
        cnt+=1
    if a[i]==c1:
        ans+=cnt
print(ans)
