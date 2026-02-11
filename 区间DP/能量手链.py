# iridescent_sly time:15:47 date:2024/5/20
N=510
f=[[0]*N for _ in range(N)]
n=int(input())
a=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    a.append(a[i])
    '''重复存储将环转换为链'''
a.append(a[1])
a=a+[0]*100

maxn=-1
for le in range(2,n+1):
    for l in range(1,2*n+1-le+1):
        r=l+le-1
        f[l][r]=0
        for k in range(l,r):  # k只能取到r-1
            f[l][r]=max(f[l][r],f[l][k]+f[k+1][r]+a[l]*a[k+1]*a[r+1])
            #print('f[%d][{%d}]='%(l,r),f[l][r],' f[%d][%d]='%(l,k),f[l][k],' f[k+1][r]=',f[k+1][r], 'a[l]*a[k+1]*a[r+1]=',a[l]*a[k+1]*a[r+1] )
        if le==n and f[l][r]>maxn:
            maxn=f[l][r]
print(maxn)
#
# maxn = -1
# dp = [[0]*300 for _ in range(300)]
# #def main():
# #global maxn
# n = int(input())
# e_input = input().split()
# e = [0] * 601
# for i in range(1, n + 1):
#     e[i] = int(e_input[i - 1])
#     e[i + n] = e[i]
# e[2 * n + 1] = e[1] # 将尾链接到头
# print(e)
# # 珠子由环拆分为链，重复存储一遍
# for length in range(2, n + 1):
#     for l in range(1, 2 * n - length + 2):
#         r = l + length - 1
#         dp[l][r] = 0
#         for k in range(l, r):
#             # k是项链的左右区间的划分点
#             dp[l][r] = max(dp[l][r], dp[l][k] + dp[k + 1][r] + e[l] * e[k + 1] *e[r + 1])
#             # 状态转移方程：max(原来能量，左区间能量+右区间能量+合并后生成能量）
#         if length == n and dp[l][r] > maxn:
#             maxn = dp[l][r] # 求最大值
# print(maxn)