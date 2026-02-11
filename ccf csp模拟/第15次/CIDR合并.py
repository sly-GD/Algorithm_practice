# # iridescent_sly time:20:06 date:2024/5/29
# n=int(input())
# a=[]
# for _ in range(n):
#     x=list(input().split('.'))
#     #print(x)
#     x=x+list(x[-1].split('/'))
#     x=x[:3]+x[4:]
#     a.append(list(map(int,x)))
#     if '/' in x:
#         a=x.find('/')
#         a=x[a+1]
#     for i in range(len(x)):
#         pass
# a.sort(key=lambda x: (x[0],x[-1]))
# # print(a)
# for i in range(len(a)):
#     print(str(a[i][0])+'.'+str(a[i][1])+'.'+str(a[i][2])+'.'+str(a[i][3])+'/'+str(a[i][-1]))


n = int(input())
ips = []
for i in range(n):
    ip = input()
    if '/' in ip:
        ip, length = ip.split('/')
        length = int(length)
    else:
        length = ip.count('.') * 8 + 8
    ip = [int(item) for item in ip.split('.')]
    ip += [0] * (4 - len(ip))
    '''计算开始地址和结束地址，合并'''
    begin = ip[0] * 16777216 + ip[1] * 65536 + ip[2] * 256 + ip[3]

    end = begin + pow(2, 32 - length)
    ip += [length, begin, end]
    ips.append(tuple(ip))

ips.sort()
# print(ips)
i = 0
while i < len(ips) - 1:
    if ips[i][-2] <= ips[i + 1][-2] and ips[i][-1] >= ips[i + 1][-1]:
        del ips[i + 1]
    else:
        i += 1

i = 0
while i < len(ips) - 1:
    if ips[i][-1] == ips[i + 1][-2] and ips[i][-3] == ips[i + 1][-3] and ips[i][-2] % pow(2, 33 - ips[i][-3]) == 0:
        ips.insert(i, ips[i][:4] + (ips[i][-3] - 1, ips[i][-2], ips[i + 1][-1]))
        '''拼接IP地址'''
        del ips[i + 1]
        del ips[i + 1]
        i = i - 1 if i != 0 else 0
    else:
        i += 1

for ip in ips:
    print(str(ip[0])+'.'+str(ip[1])+'.' + \
          str(ip[2])+'.'+str(ip[3])+'/'+str(ip[4]))