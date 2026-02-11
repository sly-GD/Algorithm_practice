# iridescent_sly time:17:41 date:2024/5/8
'''
base = 131
MOD = int(1e9 + 7)

str = input()
p = [1]
h1 = [0]
h2 = [0]
n = len(str) * 2 + 1
s = list(" " + str + str + " ")
for i in range(n - 1, 0, -2):
    s[i + 1] = "{"
    s[i] = s[i // 2]
s[1] = "{"
#print(ord('{'),ord("}"),ord('z'))
for i in range(1, n + 1):
    h1.append((h1[i - 1] * base + ord(s[i]) - ord('a')) % MOD)
    h2.append((h2[i - 1] * base + ord(s[n-i+1]) - ord('a')) % MOD)
    p.append(p[i - 1] * base % MOD)


def get(l, r):
    return (h1[r] - h1[l - 1] * p[r - l + 1] % MOD + MOD) % MOD


def get2(l, r):
    #此时l>r求解逆向的哈希值
    l, r = n - l + 1, n - r + 1
    return (h2[r] - h2[l - 1] * p[r - l + 1] % MOD + MOD) % MOD  # r-l也是负的逆向取p


ans = 0
for i in range(1, n + 1):
    l, r = 0, min(i - 1, n - 1)
    while l < r:
        mid = l + r + 1 >> 1
        if get(i - mid, i - 1) != get2(i + mid, i + 1):
            r = mid - 1
        else:
            l = mid
    len = i - l - 1
    if get(1, len) == get2(n, n - len + 1):
        if s[i - l] <= 'z':
            ans = max(ans, l + 1 + len // 2 * 2)
        else:
            ans = max(ans, l + len // 2 * 2)
    len = n - (i + l)
    if get(1, len) == get2(n, n - len + 1):
        if s[i - l] <= 'z':
            ans = max(ans, l + 1 + len // 2 * 2)
        else:
            ans = max(ans, l + len // 2 * 2)
print(ans)



P, mod = 131, 1000000007
str = input()
n = len(str) * 2 + 1
s = list(' ' + str + str + ' ')
for i in range(n - 1, 0, -2):
    s[i + 1] = '{'
    s[i] = s[i // 2]
s[1] = '{'
p = [1]
h1 = [0]
h2 = [0]
for i in range(1, n + 1):
    h1.append((h1[i - 1] * P + ord(s[i]) - ord('a')) % mod)
    h2.append((h2[i - 1] * P + ord(s[n - i + 1]) - ord('a')) % mod)
    p.append(p[i - 1] * P % mod)
def get(l, r):
    return (h1[r] - h1[l - 1] * p[r - l + 1] % mod + mod) % mod
def get2(l, r):
    l, r = n - l + 1, n - r + 1
    return (h2[r] - h2[l - 1] * p[r - l + 1] % mod + mod) % mod
ans = 0
for i in range(1, n + 1):
    l, r = 0, min(i - 1, n - 1)
    while l < r:
        mid = l + r + 1 >> 1
        if get(i - mid, i - 1) != get2(i + mid, i + 1):
            r = mid - 1
        else:
            l = mid
    len = i - l - 1
    if get(1, len) == get2(n, n - len + 1):
        if s[i - l] <= 'z':
            ans = max(ans, l + 1 + len // 2 * 2)
        else:
            ans = max(ans, l + len // 2 * 2)
    len = n - (i + l)
    if get(1, len) == get2(n, n - len + 1):
        if s[i - l] <= 'z':
            ans = max(ans, l + 1 + len // 2 * 2)
        else:
            ans = max(ans, l + len // 2 * 2)
print(ans)
'''

P = 131
mod = int(1e9 + 7)
h1 = [0]
h2 = [0]
p = [1]

s = '#' + input()

for i in range(1, len(s)):
    h1.append((h1[i - 1] * P + ord(s[i]) - ord('a')) % mod)
    h2.append((h2[i - 1] * P + ord(s[len(s) - i]) - ord('a')) % mod)
    p.append(p[i - 1] * P)

l, r = 1, len(s) - 1

while l < len(s) and s[l] == s[r]:
    l += 1
    r -= 1

'''此时有l-1位相同前后缀'''

maxn = len(s) - 1 - l + 1


def cal():
    res = 0
    for i in range(maxn, 0, -1):
        '''从前缀里找'''
        if h1[l - 1 + i] - h1[l - 1] * p[i] == h2[r] - h2[r - i] * p[i]:
            res = max(res, i)
        '''从后缀里找'''
        if h2[l - 1 + i] - h2[l - 1] * p[i] == h1[r] - h1[r - i] * p[i]:
            res = max(res, i)
    return res


print(2 * (l - 1) + cal())
