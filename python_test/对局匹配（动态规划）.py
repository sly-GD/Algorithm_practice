n,k=map(int,input().split())
a=list(map(int,input().split()))

mx=max(a)

cnt=[0 for i in range(10**5+5)]

for i in range(n):
    cnt[a[i]]+=1

ans=0
if k==0:
    for i in range(n):
        if cnt[i]!=0:
            ans+=1
    print(ans)

else :
    for i in range(k):
        p=0
        val,dp=[0 for i in range(mx)],[0 for i in range(mx)]
        for j in range(i,mx+1,k):
            val[p]=cnt[j]
            p+=1

        dp[0]=val[0]
        dp[1]=max(val[0],val[1])
        print(p)
        print(val)
        for j in range(2,p):
            dp[j]=max(dp[j-1],dp[j-2]+val[j])
        ans+=dp[p-1]
print(ans)
