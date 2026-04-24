/*
 * @lc app=leetcode.cn id=1695 lang=cpp
 *
 * [1695] 删除子数组的最大得分
 */
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = 0;
        int ans = 0,total = 0;
        int cnt[100001]={0};
        while (right < n) {
            cnt[nums[right]]++;
            ans+=nums[right];
            while (cnt[nums[right]] > 1) {
                cnt[nums[left]]--;
                ans-=nums[left];
                left++;
            }
            total = max(ans,total);
            right++;
        }
        return total;
    }
};
// @lc code=end

