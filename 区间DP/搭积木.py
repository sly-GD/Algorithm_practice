# iridescent_sly time:17:06 date:2024/5/20
mod=int(1e9)+7
N=105

n,m=map(int,input().split())
num=[[0]*(m+1) for _ in range(n+1)]
dp=[[[0]*(m+1) for _ in range(m+1)]for _ in range(n+1)]
sum_dp=[[0]*(m+1) for _ in range(m+1)]

'''初始换每一行前缀，构成新的图纸'''
for i in range(1,n+1):
    s=input()
    for j in range(1,m+1):
        num[i][j]=num[i][j-1]+(s[j-1]=='X')

ans=1
'''计算最下一层的方案数'''
for l in range(1,m+1):
    for r in range(l,m+1):
        dp[n][l][r]=int(num[n][r]-num[n][l-1]==0)
        ans=(ans+dp[n][l][r]+mod)%mod


'''从倒数第二层开始计算'''
for i in range(n-1,0,-1):
    for l in range(1,m+1):
        for r in range(1,m+1):
            sum_dp[l][r]=(dp[i+1][l][r]+sum_dp[l][r-1]+
                          sum_dp[l-1][r]-sum_dp[l-1][r-1])%mod
    for l in range(1,m+1):
        for r in range(l,m+1):
            if num[i][r]-num[i][l-1]==0: # 判断位置是否连续
                dp[i][l][r]=(sum_dp[l][m]-sum_dp[0][m]-sum_dp[l][r-1]
                             +sum_dp[0][r-1])%mod
                ans=(ans+dp[i][l][r]+mod)%mod
print((ans+mod)%mod)