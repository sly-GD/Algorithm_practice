/*
 * @lc app=leetcode.cn id=2779 lang=cpp
 *
 * [2779] 数组的最大美丽值
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        int n = nums.size();  // 获取数组长度
        // 将数组排序，以便使用滑动窗口算法
        sort(nums.begin(), nums.end());
        int left = 0, right = 0;  // 定义滑动窗口的左右边界
        int res = 0;  // 用于存储结果，即最大美丽值
        // 使用滑动窗口遍历数组
        while (right < n){
            // 如果当前窗口内的最大值和最小值的差不超过2*k，
            // 则更新结果为当前窗口大小和之前结果的最大值
            if (nums[right] - nums[left]<= 2*k){
                res = max(res, right - left+1);
            }
            else{
                // 如果差值超过2*k，则移动左边界缩小窗口
                left++;
            }
            // 移动右边界扩大窗口
            right++;
        }
        return res;  // 返回最终结果
    }
};
// @lc code=end

