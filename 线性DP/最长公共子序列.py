# iridescent_sly time:16:35 date:2024/5/12
a=input()
b=input()
dp=[[0]*210 for i in range(210)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[len(a)][len(b)])