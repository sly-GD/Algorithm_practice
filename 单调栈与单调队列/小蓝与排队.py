# iridescent_sly time:17:20 date:2024/5/6
n = int(input())

a = list(map(int, input().split()))
stack = []
a.append(float('inf'))
ans = 0

for i in range(n+1):
    '''要加上最后一个哨兵才能完整遍历计数'''
    while stack and a[i] >= a[stack[-1]]:
        ans = ans + (i - stack[-1] - 1)
        stack.pop()
    stack.append(i)

print(ans)

n = int(input())
h = [0] * 100005
ans = 0
s = []
input_line = input().split()
for i in range(1, n + 2):
    if i < n + 1:
        h[i] = int(input_line[i - 1])
    else:
        h[i] = float('inf')
    while s and h[s[-1]] <= h[i]:
        # s.top() 能看到 i 前面一个人
        ans += i - s[-1] - 1
        s.pop() # s 统计完了，出去
    s.append(i)
print(ans)