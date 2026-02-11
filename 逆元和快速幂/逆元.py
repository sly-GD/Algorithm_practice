# iridescent_sly time:21:04 date:2024/5/30
p=2146516019

ans=1
inv=[0]*(233333333+100)
inv[1]=1 # 1的逆元就是1
for i in range(2,233333333+1):
    inv[i]=(p-p//i)*inv[p%i]%p
    ans^=inv[i]

print(ans)