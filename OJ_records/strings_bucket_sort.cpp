#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// 字符串桶排序（按首字符ASCII分桶，桶内用快速排序）
void bucketSort(std::vector<std::string>& strs) {
    if (strs.empty()) return;

    // 初始化桶：ASCII 0-127 共128个桶（覆盖所有可见/不可见字符）
    const int BUCKET_COUNT = 128;
    std::vector<std::vector<std::string>> buckets(BUCKET_COUNT);

    // 1. 分配字符串到对应桶
    for (const std::string& s : strs) {
        int bucket_idx = s.empty() ? 0 : static_cast<unsigned char>(s[0]);
        buckets[bucket_idx].push_back(s);
    }

    // 2. 桶内排序 + 合并结果
    strs.clear();
    for (auto& bucket : buckets) {
        std::sort(bucket.begin(), bucket.end()); // 桶内细排序
        strs.insert(strs.end(), bucket.begin(), bucket.end());
    }
}

int main() {
    // 测试用例
    std::vector<std::string> strs = {"banana", "apple", "cherry", "date", 
                                    "apple", "", "zebra", "123", "987"};

    // 排序前
    std::cout << "排序前：";
    for (const std::string& s : strs) std::cout << "\"" << s << "\" ";
    std::cout << "\n";

    // 执行排序
    bucketSort(strs);

    // 排序后
    std::cout << "排序后：";
    for (const std::string& s : strs) std::cout << "\"" << s << "\" ";
    std::cout << "\n";

    return 0;
}