# iridescent_sly time:17:58 date:2024/5/26
import sys

N = 100
Q = [[0] * N for _ in range(N)]
n = int(input())
for _ in range(n):
    a = list(sys.stdin.readline().strip().split())
    # print(a)
    #    flag=0
    f1 = 1
    yuansu = []
    for i in range(1, len(a)):
        x = ''
        for j in range(len(a[i])):
            if 'a' <= a[i][j] <= 'z':
                x += a[i][j]
            if '0' <= a[i][j] <= '9':
                yuansu.append((i, x, a[i][j]))
                x = ''

        # f2=1
        # for u in yuansu:
        #     A[f1][0]=u[0]
        #     A[f1][f2]=u[1]
        #     f2+=1
        #
    temp = ['']
    f3 = 1
    for i in yuansu:
        if i[1] not in temp:
            temp.append(i[1])

            Q[f3][i[0]] = int(i[2])
            f3 += 1
        else:
            Q[temp.index(i[1])][i[0]] = int(i[2])

    # print(yuansu)
    x = []
    for _ in Q[:len(temp)]:
        x.append(_[:len(a)])

    for _ in range(len(x[0])):
        x[0][_]=0
    #print(x)
    import math


    def swap_rows(matrix, i, j):
        matrix[i], matrix[j] = matrix[j], matrix[i]


    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)


    def Rank(matrix, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return 0

        flag = 0
        for i in range(x1, x2 + 1):
            if matrix[i][y1] != 0:
                flag = i
                break

        if flag == 0:
            return Rank(matrix, x1, y1 + 1, x2, y2)

        swap_rows(matrix, x1, flag)

        for i in range(x1 + 1, x2 + 1):
            if matrix[i][y1] == 0:
                continue
            LCM = lcm(matrix[x1][y1], matrix[i][y1])  # 由于flag已经被x1替换，这里使用matrix[x1]
            t2 = LCM // matrix[x1][y1]
            t1 = LCM // matrix[i][y1]  # 这里使用matrix[x1]，因为flag已经是x1了
            for j in range(y1, y2 + 1):
                matrix[i][j] = matrix[i][j] * t1 - matrix[x1][j] * t2

        return Rank(matrix, x1 + 1, y1 + 1, x2, y2) + 1

    if Rank(x,1,1,len(x)-1,len(x[0])-1)==len(x[0])-1:
        print("N")
    else:
        print("Y")
    #print(Rank(x, 1, 1, len(x) - 1, len(x[0]) - 1))
    # 示例用法
    # 假设matrix是一个r x c的二维列表，你需要先初始化它
    # r, c = ... # 定义行数和列数
    # matrix = [[... for _ in range(c)] for _ in range(r)] # 初始化矩阵

    # 然后你可以调用Rank函数
    # result = Rank(matrix, 1, 1, r-1, c-1)
    #
    # def gaussian_elimination_and_rank(A):
    #     n = len(A)
    #     m=len(A[0])
    #     # 执行高斯消元（不需要存储增广矩阵b，因为我们只关心秩）
    #     for i in range(n):
    #         # 寻找当前列下的最大主元
    #         max_row = i
    #         for j in range(i + 1, n):
    #             if abs(A[j][i]) > abs(A[max_row][i]):
    #                 max_row = j
    #
    #                 # 交换最大主元所在的行到当前行
    #         print(A)
    #         A[i], A[max_row] = A[max_row], A[i]
    #         print(A)
    #         # 当前行主元为0，则跳过该行（不会影响秩）
    #
    #         if i<=m-1 and A[i][i] == 0:
    #             continue
    #
    #             # 消元
    #         for j in range(i + 1, n):
    #             factor = A[j][i] // A[i][i]
    #             for k in range(i, len(A[0])):
    #                 A[j][k] -= factor * A[i][k]
    #
    #                 # 计算秩：非零行的数量
    #     r = 0
    #     for i in range(n):
    #         if any(A[i]):  # 如果当前行有非零元素
    #             r += 1
    #
    #     return r
    #
    #
    # rank = gaussian_elimination_and_rank(x)
    #
    # if print("矩阵的秩为:", rank)
