# # iridescent_sly time:19:27 date:2024/5/18
# from collections import deque
# c,m,n=map(int,input().split())
# a=[0]*(c+1)
# s=set()
# for i in range(m):
#     x,y=map(int,input().split())
#     a[x]=y
#     s.add(x)
#
#
# def dishui(u):
#     #print(a)
#     a[u]+=1
#     if a[u]>=5:
#         a[u]=0
#         f, g = 0, 0
#         for i in range(len(a)):
#
#             if u-i>0 and a[u-i]!=0 and f==0:
#                 #print('u-i',i,u-i)
#                 f=1
#                 a[u-i]+=1
#                 #dishui(u-i)
#             if u+i<=c and a[u+i]!=0 and g==0:
#                 g=1
#                 #print('u+i',i,u+i)
#                 a[u+i]+=1
#
#                 #dishui(u+i)
#             if f==1 and g==1:
#                 break
#     for i in range(len(a)):
#         if a[i]>=5:
#             dishui(i)
# for i in range(n):
#     x=int(input())
#     dishui(x)
#     print(c-a.count(0)+1)
#     #print(a)

from heapq import heappush, heappop
##  heapq 小顶堆，完全二叉树 层序遍历保存
from collections import defaultdict

# 使用defaultdict来存储位置和它们的数字
h=[0]
# 使用列表作为优先队列的底层容器
q = []
# 使用集合来存储所有位置
s = set()


def bfs():
    global s
    while q:
        t = heappop(q)[1]  # 堆中存储的是(数字, 位置)的元组，我们关心的是位置t
        if h[t] >= 5:
            h[t] = 0
            # 检查左侧和右侧的位置
            s=list(s)
            s.sort()
            i=s.index(t)
            if i-1 >=0:
                h[s[i-1]] += 1
                heappush(q, (h[s[i-1]], s[i-1]))  # 将更新后的(数字, 位置)元组加入队列
            if i+1<len(s):
                h[s[i+1]] += 1
                heappush(q, (h[s[i+1]], s[i+1]))
            s=set(s)
            s.remove(t)


def main():
    global h
    c, m, n = map(int, input().split())  # 读取c, m, n
    h = [0]*(c+20)
    for _ in range(m):
        pos, nums = map(int, input().split())
        h[pos] = nums
        s.add(pos)

    for _ in range(n):
        op = int(input())
        h[op] += 1
        heappush(q, (h[op], op))  # 将(数字, 位置)元组加入队列

        bfs()
        print(len(s))


if __name__ == "__main__":
    main()