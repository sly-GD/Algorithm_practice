# iridescent_sly time:16:45 date:2024/5/13
import sys

n,l,k=map(int,input().split())

d=[0]+list(map(int,input().split()))+[l]
a=[0]+list(map(int,input().split()))

dp=[[sys.maxsize]*(k+1) for i in range(n+2)]

for i in range(k+1):
    dp[1][i]=0

for i in range(2,n+2):
    for j in range(min(k,i)+1):
        for c in range(j+1):
            dp[i][j]=min(dp[i][j],dp[i-c-1][j-c]+(d[i]-d[i-c-1])*a[i-c-1])
mi=sys.maxsize
for i in range(k+1):
    mi=min(mi,dp[n+1][i])
print(mi)

