# iridescent_sly time:20:07 date:2024/5/30
# print(999%98)
# print(999%2)
f=[]
n=int(input())
# for _ in range(n):
#     f=[]
#     a,b=map(int,input().split())
#     if b-a>2:
#         print("Yes")
#         continue
#     flag=True
#     for i in range(2,b+1):
#         if not flag:
#             break
#         for j in range(i+1,b+1):
#             if a%i==a%j:
#                 flag=False
#                 print("Yes")
#                 break
#     if flag==True:
#         print("No")


'''
反证法，即不存在两个数使得nmodx = nmody
则一定满足n%1 = 0, n % 2 = 1,....n%m = m - 1
不存在
否则存在
'''

for _ in range(n):
    a,b=map(int,input().split())
    flag=True
    for i in range(2,b+1):
        if a%i!=i-1:
            print("Yes")
            flag=False
            break
    if flag:
        print("No")