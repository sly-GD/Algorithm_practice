# iridescent_sly time:17:39 date:2024/5/28


from collections import deque


def bfs(start, times, arr):
    q = deque()
    V[start] += 1
    q.append(start)
    while q:
        x = q.popleft()
        for y in a[x]:
            #print(y)
            if V[y] == times:
                continue
            arr[y] = arr[x] + 1
            V[y] += 1
            q.append(y)


N = 50000
RT = [0] * N
RF = [0] * N
RN = [0] * N
'''
RT,RF,RN 分别表示三点到其他各点的距离
在V中统计每个点被访问的次数
恰好在三次bfs中被访问三次的点为公共点。v[i]==3
V[i]==0 的点为隔绝点
'''
a = [[]*N for _ in range(N)]
V = [0] * N


def main():
    TE, FE, S = map(int, input().split())
    T, F, n, m = map(int, input().split())
    for _ in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    #print(a[:20])
    bfs(n, 1, RN)
    if not V[T] or not V[F]:
        print(-1)
        return
    bfs(T, 2, RT)
    bfs(F, 3, RF)  # 3 表示节点访问次数，必须三个节点访问才行
    ans = float('inf')
    for i in range(n + 1):
        if V[i]:
            ans = min(ans, RT[i] * TE + RF[i] * FE + RN[i] * (TE + FE - S))
    print(ans)
    return
    # code here


if __name__ == '__main__':
    main();