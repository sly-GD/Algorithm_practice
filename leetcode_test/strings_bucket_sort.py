def string_bucket_sort_lowercase(arr):
    """仅处理小写字符的字符串桶排序（实现a<ab<b）"""
    if not arr:
        return []

    def msd_sort(strings, pos):
        #print(f"pos={pos}, strings={strings}")
        # 基线条件：桶内元素≤1，无需排序
        if len(strings) <= 1:
            return strings
        
        # 初始化桶：0-25对应a-z，26对应「长度不足当前pos位」的字符串
        buckets = [[] for _ in range(27)]
        
        # 按第pos位字符分桶（核心：匹配字典序）
        for s in strings:
            if pos >= len(s):
                buckets[26].append(s)  # 长度不足，优先排前（如a在ab前）
            else:
                char_idx = ord(s[pos]) - ord('a')  # 小写字符转0-25索引
                buckets[char_idx].append(s)
        
        # 递归处理每个桶，合并结果（先合长度不足的桶，再合a-z桶）
        sorted_res = []
        #print(f"pos={pos}, buckets={buckets}")  # 调试输出，查看每层桶分布
        sorted_res.extend(msd_sort(buckets[26], pos + 1))  # 先加a（长度不足1位）
        for i in range(26):
            sorted_res.extend(msd_sort(buckets[i], pos + 1))  # 再加ab（a桶）、b（b桶）
        #print(f"pos={pos}, buckets={buckets}")  # 调试输出，查看每层桶分布
        #print(f"pos={pos}, sorted_res={sorted_res}")
        return sorted_res

    # 从第0位（首位）开始递归排序
    return msd_sort(arr, 0)

# 测试：验证a<ab<b
test_arr = ["b", "ab", "a", "aa", "aab"]
sorted_arr = string_bucket_sort_lowercase(test_arr)
print(sorted_arr)  # 输出：['a', 'ab', 'b']，完全符合a<ab<b的要求