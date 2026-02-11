# iridescent_sly time:16:10 date:2024/5/12
n=int(input())
N=1000010
a=[0]*N
for i in range(1,n+1):
    a[i]=list(map(int,input().split()))

dp=[0]*2*N
dp[n+1]=0
for i in range(n,0,-1):
    dp[i]=dp[i+1]
    c=i+a[i][1]+1
    dp[i]=max(dp[i],a[i][0]+dp[c])
print(dp[1])