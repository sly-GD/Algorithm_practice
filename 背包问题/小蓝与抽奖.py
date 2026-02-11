# iridescent_sly time:16:58 date:2024/5/16
n,A=map(int,input().split())

a=[0]+list(map(int,input().split()))

dp=[[[0]*2505]*55 for i in range(55) ]
dp[0][0][0]=1
for i in range(n):
    dp[i][0][0]=1

for i in range(1,n+1):
    for j in range(1,i+1):
        for k in range(1,n*A+1):
            if k>=a[i]:
                dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k-a[i]]
            else:
                dp[i][j][k]=dp[i-1][j][k]
ans=0
for i in range(1,n+1):

    ans+=dp[n][i][A*i]
print(ans)