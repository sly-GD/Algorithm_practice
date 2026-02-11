# iridescent_sly time:19:13 date:2024/5/31
a = input()
''' 改造字符串'''
s = '$#'
n = len(a)
k = 0
for _ in range(n):
    s += a[_]
    s += '#'
n = len(s) - 1
s+=' '*100
print(s)

d = [0] * (n+3)


# d[i]表示以i为中心最长回文串长度的一半
def get_d(s, n):
    d[1] = 1
    r = 1
    l = 0
    for i in range(2, n + 1):
        if i <= r:  # 盒子内加速
            d[i] = min(d[r - i + l], r - i + 1)
        # print(d)?
        while s[i - d[i]] == s[i + d[i]]:  # 暴力枚举
            d[i] += 1

            # print(d[i])
        if i + d[i] - 1 > r:  # 更新盒子
            l = i - d[i] + 1
            r = i + d[i] - 1


get_d(s, n)
print("最长回文串={}".format(max(d)//2+1))
