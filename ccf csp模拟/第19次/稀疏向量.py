# # iridescent_sly time:13:52 date:2024/5/27
# import time
#
# #t1=time.perf_counter()
# n,a,b=map(int,input().split())
# A={}
# B={}
# for _ in range(a):
#     x,y=map(int,input().split())
#     A.update({x:y})
# for _ in range(b):
#     x, y = map(int, input().split())
#     B.update({x:y})
# # print(A.keys())
# # print(B.keys())
# res=0
# for i in A.keys():
#     if i in B.keys():
#         res+=A[i]*B[i]
# print(res)

n, a, b = map(int, input().split())
A = {int(x): int(y) for _ in range(a) for x, y in [input().split()]}
B = {int(x): int(y) for _ in range(b) for x, y in [input().split()]}

res = sum(A[i] * B[i] for i in A if i in B)
print(res)