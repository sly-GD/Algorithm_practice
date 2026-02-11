#  错误答案

n,k=map(int,input().split())

a=[0]+list(map(int,input().split()))
su=[0]*(n+1)


for i in range(1,n+1):
    su[i]=su[i-1]+a[i]

print(su)
ans=0
cnt=[0]*k

cnt[0]=1 #3的倍数本身
for i in range(1,n+1):
    if su[i]>=0:
        ans+=cnt[su[i]%k]       #前缀和余数相同的区间，必定符合
        cnt[su[i]%k]+=1
print(ans)
"""
for i in range(1,len(a)):
    for j in range(i+1,len(a)):
         if (su[j]-su[i-1])%k==0 and su[j]-su[i-1]>=0:
            print(i,j)
            ans+=1
print(ans)
"""
#print(-14%3)
