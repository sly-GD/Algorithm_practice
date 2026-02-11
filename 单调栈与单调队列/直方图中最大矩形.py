# iridescent_sly time:12:58 date:2024/5/6

#print(a)
while True:
    a = list(map(int, input().split()))
    if a[0]==0 and len(a)==1:
        break
    stack=[0]
    a.append(0)
    #a.pop(0)  '''舍去第一个元素'''
    a.insert(0,0)
    #print(a)
    ans=0
    for i in range(1,len(a)):
            while stack and a[i]<a[stack[-1]]:
                mid=stack[-1]
                stack.pop()
                if stack:  #要记得判断的栈是否为空，，警惕任何取元素之后
                    width=i-stack[-1]-1
                    ans=max(ans,a[mid]*width)
            stack.append(i)
    print(ans)

# iridescent_sly time:12:58 date:2024/5/6
heights = list(map(int, input().split()))
# print(a)
while heights[0] != 0 or len(heights) != 1:
        # Monotonic Stack
        '''
        找每个柱子左右侧的第一个高度值小于该柱子的柱子
        单调栈：栈顶到栈底：从大到小（每插入一个新的小数值时，都要弹出先前的大数值）
        栈顶，栈顶的下一个元素，即将入栈的元素：这三个元素组成了最大面积的高度和宽度
        情况一：当前遍历的元素heights[i]大于栈顶元素的情况
        
        情况二：当前遍历的元素heights[i]等于栈顶元素的情况
        情况三：当前遍历的元素heights[i]小于栈顶元素的情况
        '''

        # 输入数组首尾各补上一个0（与42.接雨水不同的是，本题原首尾的两个柱子可以作为核心柱进行最大面积尝试
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0
        for i in range(1, len(heights)):
            # 情况一
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            # 情况二
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            # 情况三
            else:
                # 抛出所有较高的柱子
                while stack and heights[i] < heights[stack[-1]]:
                    # 栈顶就是中间的柱子，主心骨
                    mid_index = stack[-1]
                    stack.pop()
                    if stack:
                        left_index = stack[-1]
                        right_index = i
                        width = right_index - left_index - 1
                        height = heights[mid_index]
                        result = max(result, width * height)
                stack.append(i)
        print(result)

        heights= []
        heights = list(map(int, input().split()))


def solve(ls: list) -> int:
    st, area = [], 0
    for i in range(len(ls)):
        while st and ls[i] < ls[st[-1]]:
            top = st.pop()
            area = max(area, ls[top] * (i - st[-1] - 1))
        st.append(i)
    return area
if __name__ == '__main__':
    res = []
    while True:
        ls = list(map(int, input().split()))
        if not ls[0]:
            break
        else:
            res.append(solve([0] + ls[1:] + [0]))
    for r in res:
        print(r)