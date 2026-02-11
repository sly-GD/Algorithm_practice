# iridescent_sly time:15:11 date:2024/5/27
n, m = map(int, input().split())
qujian = []
xishu = []
res = 0
flag=[False]*10
for _ in range(n):
    tem=[]
    l, r, a, b, c = map(int, input().split())
    qujian.append((l, r))
    xishu.append((a, b, c))
    for i in range(l,r+1):
        tem.append(a*i*i+b*i+c)
    res+=max(tem)
print(res)