# iridescent_sly time:19:08 date:2024/5/18
n, m = map(int, input().split())

a = list(map(str, input().split()))
b = list(map(str, input().split()))
for i in range(len(a)):
    a[i] = a[i].lower()
for j in range(len(b)):
    b[j] = b[j].lower()
a = set(a)
a = list(a)
b = set(b)
b = list(b)
cnt = 0
for i in range(len(a)):
    if a[i] in b:
        cnt += 1
res = len(a) + len(b) - cnt
print(cnt)
print(res)
