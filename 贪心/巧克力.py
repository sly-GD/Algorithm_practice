# iridescent_sly time:15:56 date:2024/5/3
import queue

x, n = map(int, input().split())
a = [[] for i in range(n)]
is_possible = False
chocolates = []
sorted_chocolates = []
queue_length = [0] * x
for i in range(n):
    a, b, c = list(map(int, input().split()))
    if b >= x:
        is_possible = True
    chocolates.append([a, -b, c])
    sorted_chocolates.append([-b, a, c])

chocolates.sort()
sorted_chocolates.sort()
total_chocolates = 0
queue_items = 0

print(chocolates)
print()
print(sorted_chocolates)
def consume_chocolates():
    global x, total_chocolates, queue_items
    q = queue.PriorityQueue()
    i = 0
    queue_length_q = 0

    while x:
        for i in range(i, len(sorted_chocolates) + 1):
            if i == len(sorted_chocolates):
                i = i
                break
            b, a, c = sorted_chocolates[i]
            b = -b
            if b >= x:
                q.put([a, -c, b])  # 因为优先队列优先级越小在前面
                queue_length_q += 1
            else:
                i = i
                break
        print(i)
        print('x={}'.format(x))
        for it in q.queue:
            print(it)

        a, c, b = q.get()
        print('取出',[a,c,b])
        c = -c
        queue_length_q -= 1
        x -= 1
        total_chocolates += a
        if x == 0:
            return True
        if c != 1:
            q.put([a, -c + 1, b])
            queue_length_q += 1
        if queue_length_q == 0:
            break

    return False


if not is_possible:
    print(-1)
else:
    if consume_chocolates():
        print(total_chocolates)
    else:
        print(-1)
