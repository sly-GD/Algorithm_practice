# # iridescent_sly time:14:18 date:2024/5/27
# import io
# import sys
#
# w = int(input())
# s = sys.stdin.readline()
# cnt = 0
# print(s)
# def spaceLine(x):
#     for i in range(len(x)):
#         if s[i]!=' ':
#             return False
#     return True
# while s:
#     # s=sys.stdin.readline()
#     # print(s)
#     if len(s) <= w:
#         if spaceLine(s):
#             cnt += 1
#     s = sys.stdin.readline()
#         #continue
#
# print(cnt)
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import namedtuple
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        alist = []
        for i in range(len(List)):
            alist.append([])
            for j in range(len(List[i])):
                alist[i].append(List[i][j].val)
        h = list()
        res = list()
        heapContent = namedtuple('contents', ('elem', 'array_idx', 'array_elem_idx'))
        for i, k in enumerate(alist):
            heapq.heappush(h, heapContent(k[0], i, 1))
        total_elems = len(alist) * len(alist[0])
        for _ in range(0, total_elems):
            popped = heapq.heappop(h)
            if popped.elem == float('inf'):
                continue
            res.append(popped.elem)
            next_array = popped.array_idx
            next_elem_idx = popped.array_elem_idx
            if next_elem_idx < len(alist[next_array]):
                heapq.heappush(h, heapContent(alist[next_array][next_elem_idx], \
                                              next_array, next_elem_idx + 1))
            else:
                heapq.heappush(h, heapContent(float('inf'), next_array, float('inf')))
        return res
