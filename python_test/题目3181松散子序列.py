s=input()
def value(c):
    return ord(c)-ord('a')+1


dp=[[0,0] for i in range(len(s))]
dp[0][1]=value(s[0])

for i in range(1,len(s)):
    dp[i][0]=max(dp[i-1][0],dp[i-1][1])
    dp[i][1]=dp[i-1][0]+value(s[i])

print(max(dp[-1][0],dp[-1][1]))
