/*
 * @lc app=leetcode.cn id=1004 lang=cpp
 *
 * [1004] 最大连续1的个数 III
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size();
        int left = 0, right = 0, ans = 0;
        int cnt = 0;
        while (right < n) {
            if (nums[right] == 0) cnt++;
            while (cnt > k) {
                if (nums[left] == 0) cnt--;
                left++;
            }
            ans = max(ans, right - left + 1);
            right++;
        }
        return ans;
    }
};
// @lc code=end

