# iridescent_sly time:20:42 date:2024/5/19
n = int(input())
for _ in range(n):
    x = input()
    s = eval(x.replace('x', '*').replace('/', '//'))
    if s == 24:
        print('Yes')
    else:
        print('No')
