# iridescent_sly time:17:31 date:2024/5/12
n=int(input())
a=list(map(int,input().split()))
N=1010
dp=[1]*N

i=1
ans=0
for i in range(1,len(a)):
    for j in range(i):
        if a[j]<a[i]:
            dp[i]=max(dp[j]+1,dp[i])
            ans=max(ans,dp[i])
print(ans)
