# iridescent_sly time:19:16 date:2024/5/12
n, m = map(int, input().split())
from itertools import permutations

'''递归'''
'''
ans=0
def f(a,b,c):
    global ans
    if a>0:
        f(a-1,b,c*2)
    if b>0:
        f(a,b-1,c-1)
    if a==0 and b==0 and c==1: #最后必定遇花
        ans+=1
f(n,m-1,2)
print(ans)
'''

'''全排列'''

a = [-1] * m + [2] * n
ans = 0
res = permutations(a)
for i in res:
    if i[len(a) - 1] != -1:
        continue
    # print(i)
    x = 2
    for j in i:
        # print(j)
        if j == -1:
            x += j
        if j == 2:
            x *= j
            if x > m:
                break
    if x == 0 and i[len(a) - 1] == -1:
        print("jiayi")
        ans += 1
print(ans)
