# iridescent_sly time:13:54 date:2024/5/5
n = int(input())
a = [[] for i in range(n)]
s = []
for i in range(n):
    a[i] = list(map(int, input().split()))
    s.append((sum(a[i]), a[i][0] + a[i][1]))
s.sort(key=lambda x: (x[0]))
#print(s)
ans = 0
for i in range(n):
    for j in range(i):
        ans += s[j][0]
        #print(i,ans)
    ans += s[i][1]
print(ans)
