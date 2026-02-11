# iridescent_sly time:16:38 date:2024/5/10
n, m, k = map(int, input().split())
'''从n个字符串中找出m个字符串（组合），并且列加每个组合中长度大于k的相同字串个数'''
s=['#']*100010
pw=[0]*100010
d=[0]*100010
l=[0]*100010
r=[[0]*100010 for i in range(6)]

c={'A':1,'G':2,'C':3,'T':4}
mod=int(1e9+7)

len_s=[0]*6
ans=0

mp=[{} for _ in range(100010)]
dr={}
wl=0

def qpow(x,p):
    ans=1
    while p:
        if p&1:
            ans=ans*x%mod
        x=x*x%mod
        p>>=1
    return ans
pw[0]=1
for i in range(1,100010):
    pw[i]=pw[i-1]*5%mod
d[100000]=qpow(pw[100000],mod-2)
for i in range(99999,-1,-1):
    d[i]=d[i+1]*5%mod

for i in range(1,n+1):
    s[i]=input()
    len_s[i]=len(s[i])
    for j in range(1,len_s[i]+1):
        r[i][j]=(r[i][j-1]+c[s[i][j-1]]*pw[j-1]%mod)%mod
    for j in range(1,len_s[i]-k+2):
        qwq=(r[i][j+k-1]-r[i][j-1]+mod)%mod*d[j-1]%mod
        if qwq not in dr:
            dr[qwq]=1
            wl+=1
            l[wl]=qwq
        mp[i][qwq]=mp[i].get(qwq,0)+1
'''
print(mp[:10])
print(dr)
print(wl)
for i in range(1,len(r)):
    print(r[i][:10])
'''
e=2**n
for i in range(1,wl+1):
    for j in range(e):
        if bin(j).count('1')!=m:
            continue
        e_val=1
        for c in range(1,n+1):
            if j & (1<<(c-1)):
                e_val=e_val*mp[c].get(l[i],0)%mod
        ans=(ans+e_val)%mod
print(ans)