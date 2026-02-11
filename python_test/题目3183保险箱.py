n=int(input())
x=input()
y=input()

x,y=list(map(int,x))[::-1],list(map(int,y))[::-1]
dp=[[0]*3 for i in range(n)]
dp[0][0]=abs(x[0]-y[0])
dp[0][1]=10-x[0]+y[0]   #进位
dp[0][2]=10-y[0]+x[0]   #退位



for i in range(1,n):
    dp[i][0]=min(dp[i-1][0]+abs(x[i]-y[i]),dp[i-1][1]+abs(x[i]+1-y[i]),dp[i-1][2]+abs(x[i]-1-y[i]))
    dp[i][1]=min(dp[i-1][0]+10-x[i]+y[i],dp[i-1][1]+9-x[i]+y[i],dp[i-1][2]+11-x[i]+y[i])
    dp[i][2]=min(dp[i-1][0]+10-y[i]+x[i],dp[i-1][1]+11-y[i]+x[i],dp[i-1][2]+9-y[i]+x[i])

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))
#for i in dp:
#    print(i)
