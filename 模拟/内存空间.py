# # iridescent_sly time:10:28 date:2024/5/7
# t = int(input())
# ans = 0
# while t != 0:
#     a = ''
#     a = input()
#     # print(a[:3],a[:4])
#     if '[' not in a:
#         if a[:3] == 'int':
#             ans += a.count('=') * 4
#         elif a[:4] == 'long':
#             ans += a.count('=') * 8
#         else:
#             flag = 0
#             for i in range(len(a)):
#                 if flag == 1 and a[i]!='"':
#                     ans += 1
#                 if a[i] == '"' and flag == 0:
#                     flag = 1
#                     continue
#                 if a[i] == '"' and flag == 1:
#                     flag = 0
#     else:
#         te = 0
#         y = ''
#         x = 0
#         flag = 0
#         if a[:3] == 'int':
#             x = 4
#         else:
#             x = 8
#         for i in range(6, len(a)):
#             if flag == 1 and a[i] != ']':
#                 y += a[i]
#             if a[i] == "[":
#                 flag = 1
#             if a[i] == "]":
#                 flag = 0
#                 # print(y)
#                 te += int(y) * x
#                 y = ''
#         ans += te
#     t -= 1
#
#
# def solve(x):
#     b = x % 1024
#     kb = (x // 1024) % 1024
#     mb = (x // (1024 * 1024)) % 1024
#     gb = (x // (1024 * 1024 * 1024)) % 1024
#     res = ''
#     if gb:
#         res += str(gb) + "GB"
#     if mb:
#         res += str(mb) + "MB"
#     if kb:
#         res += str(kb) + "KB"
#     if b:
#         res += str(b) + "B"
#     print(res)
#
#
# solve(ans)
#
import os
import sys

# 请在此输入您的代码
s = 0
n = int(input())
for i in range(n):
    a = input()
    if 'int' in a and '[' not in a:
        s += a.count('=') * 4
    elif 'long' in a and ']' not in a:
        s += a.count('=') * 8
    elif '"' in a:
        x = a.split('"')
        # print(x)
        for i in range(len(x)):
            if '=' in x[i]:
                s += len(x[i + 1])
    else:
        if 'long' in a:
            t=8
        elif 'int' in a:
            t=4
        x = a.split('[')
        # print(x)
        for i in range(len(x)):
            if '=' in x[i]:
                s += int(x[i + 1][:x[i+1].find(']')])*t

    # print(s)
def zhuan(x):
    res = ''
    b = x % 1024
    kb = (x // 1024) % 1024
    mb = (x // (1024 * 1024)) % 1024
    gb = (x // (1024 ** 3)) % 1024

    if gb > 0:
        res += str(gb) + 'GB'
    if mb > 0:
        res += str(mb) + 'MB'
    if kb > 0:
        res += str(kb) + 'KB'
    res += str(b) + 'B'
    return res


print(zhuan(s))


s='owowo'
x=s.find('owo')
print(s.find('owo',x+1))
print()