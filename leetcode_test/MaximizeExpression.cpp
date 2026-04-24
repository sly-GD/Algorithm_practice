#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

/**
 * 题目：通过添加括号最大化加减法表达式的值
 * 时间复杂度：O(n)
 * 空间复杂度：O(n) - 可以优化到 O(1)
 */
long long solveMaxExpression(const vector<int>& nums, const vector<char>& ops) {
    int n = nums.size();
    // dp[i][j] 表示处理到第 i 个数字，有 j 个开启的减号括号时的最大值 (j=0,1,2)
    // 初始化为极小值
    const long long INF = 1e18;
    vector<vector<long long>> dp(n + 1, vector<long long>(3, -INF));

    // 第一个数字前面没有符号，始终为正，且此时没有括号
    dp[1][0] = nums[0];

    for (int i = 1; i < n; ++i) {
        char op = ops[i - 1];
        int val = nums[i];

        for (int j = 0; j < 3; ++j) {
            if (dp[i][j] == -INF) continue;

            // 确定当前数字在当前括号层数下的“实际符号”
            // j=0: 保持原样; j=1: 翻转; j=2: 再次翻转(正常)
            int effective_sign;
            if (j == 1) effective_sign = (op == '+' ? -1 : 1);
            else effective_sign = (op == '+' ? 1 : -1);

            long long current_val = dp[i][j] + (long long)effective_sign * val;

            // 转移 1: 不改变括号状态（保持当前 j 层）
            dp[i + 1][j] = max(dp[i + 1][j], current_val);

            // 转移 2: 如果当前符号是减号，且括号层数未满，可以开启新括号
            // 注意：开启括号的一瞬间，当前数字的符号已经确定了，影响的是后面的数字
            if (op == '-' && j < 2) {
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], current_val);
            }

            // 转移 3: 尝试闭合括号
            // 可以在当前数字计算完后，闭合 1 个或多个括号
            if (j > 0) {
                dp[i + 1][j - 1] = max(dp[i + 1][j - 1], current_val); // 闭合一个
                if (j == 2) dp[i + 1][0] = max(dp[i + 1][0], current_val); // 闭合两个
            }
        }
    }

    // 最终结果是处理完所有数字，且所有括号都已闭合（状态0）
    // 实际上在加减法中，最后不闭合也没关系，取所有 j 的最大值即可
    return max({dp[n][0], dp[n][1], dp[n][2]});
}

int main() {
    // 示例: 1 + 3 - 2 - 5 + 1 - 6 + 7
    vector<int> nums = {1, 3, 2, 5, 1, 6, 7};
    vector<char> ops = {'+', '-', '-', '+', '-', '+'};

    long long result = solveMaxExpression(nums, ops);
    cout << "Maximum possible value: " << result << endl;
    
    // 解释：1 + 3 - (2 - 5 - (1 + 6)) + 7 = 1 + 3 - 2 + 5 + 1 + 6 + 7 = 21
    return 0;
}