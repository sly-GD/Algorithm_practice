# iridescent_sly time:18:22 date:2024/5/31
base=131
mod=212370440130137957

n=int(input())
N=10010
p=[0]*N
h=[0]*N

a=[]

for _ in range(n):
    s=' '+input()
    # print(s)
    p[0]=1
    for i in range(1,len(s)):
        p[i]=p[i-1]*base %mod
        h[i]=(h[i-1]*base + ord(s[i]))%mod
        if i==len(s)-1:
            a.append(h[i])
print(len(set(a)))


'''get字串的hash值'''
def get(l,r):
    return h[r]-h[l+1]*p[r-l+1]