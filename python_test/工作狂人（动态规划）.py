n=int(input())
a=list(map(int,input().split()))
if n%2==0:
    x=n//2
else:
    x=n//2+1
print(x)
dp=[0 for i in range(n)]
dp[0]=a[0]
dp[1]=max(a[0],a[1])
b=[]
for i in range(2,n):
    dp[i]=max(dp[i-1],dp[i-2]+a[i])
    if dp[i]>dp[i-1]:
        b.append(a[i])
        
        print(a[i],end=' ')
while True:
    if len(b)>x:
        b.remove(min(b))
    else:
        break
print(sum(b))

'''
n=int(input())
a=[0]+list(map(int,input().split()))

dp=[0 for i in range(100005)]
sum=0
for i in range(1,n+1):
    if(i%2!=0):
        dp[i]=max(a[i]+dp[i-2],sum)
    else:
        dp[i]=max(a[i]+dp[i-2],dp[i-1])
        sum+=a[i]
print(dp[n])

'''
