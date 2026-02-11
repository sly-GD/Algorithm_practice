import bisect
# 示例数据
data = [1, 2, 3, 5, 7, 9]
# 查找大于等于某个值的第一个位置
index = bisect.bisect_left(data, 4)
print("Index to insert 4:", index) # Output: 3
# 如果需要获取值而不是索引，则可以直接使用索引访问
if index < len(data):
    print("Value at index {}: {}".format(index, data[index]))
