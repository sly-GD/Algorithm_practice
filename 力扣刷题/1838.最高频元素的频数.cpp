/*
 * @lc app=leetcode.cn id=1838 lang=cpp
 *
 * [1838] 最高频元素的频数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
      int n = nums.size();
      sort(nums.begin(), nums.end());
      int high =0 ,low =0,res = 0;
      long long sum = 0;
      while(high<n){
        sum += nums[high];
        while(sum + k < (long long)nums[high]*(high-low+1)){
          sum -= nums[low];
          low++;
        }
        res = max(res,high-low+1);
        high++;
      }
      return res;
    }
};
// @lc code=end

