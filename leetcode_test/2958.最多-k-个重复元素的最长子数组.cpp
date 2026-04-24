/*
 * @lc app=leetcode.cn id=2958 lang=cpp
 *
 * [2958] 最多 K 个重复元素的最长子数组
 */
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <climits>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> mp;
        int ans = 0;
        int high = 0 , low = 0;
        while(high < n){
            mp[nums[high]]++;
            while(mp[nums[high]] > k){
                mp[nums[low]]--;
                low++;
            }
            ans = max(ans, high - low + 1);
            high++;
        }
        return ans;
    }
};
// @lc code=end

