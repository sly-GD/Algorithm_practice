# iridescent_sly time:20:16 date:2024/5/31
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
d=[0]*(len(a)+10)
s=[0]*len(a)
for i in range(1,len(a)):
    d[i]=a[i]-a[i-1]
# print(d)
for _ in range(m):
    l,r,c=map(int,input().split())
    d[l]+=c
    d[r+1]-=c
# print(d?)
for i in range(1,len(a)):
    s[i]=s[i-1]+d[i]
    print(s[i],end=" ")
# print(*s)