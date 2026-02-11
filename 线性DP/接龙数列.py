# iridescent_sly time:16:48 date:2024/5/12
n=int(input())
a=list(map(str,input().split()))
N=100010
dp=[0]*N
dp[0]=1
m=-1
for i in range(len(a)):
    x,y=int(a[i][0]),int(a[i][-1])
    dp[y]=max(dp[x]+1,dp[y])
    m=max(m,dp[y])
print(len(a)-m)