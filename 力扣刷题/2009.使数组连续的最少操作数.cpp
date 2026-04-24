/*
 * @lc app=leetcode.cn id=2009 lang=cpp
 *
 * [2009] 使数组连续的最少操作数
 */
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        //去除元素
        sort(nums.begin(),nums.end());
        auto new_end = unique(nums.begin(),nums.end());
        //nums.erase(new_end,nums.end());
        int m = new_end-nums.begin();
        int ans = 0;
        int high = 0,low = 0;
        while(high<m){
            while(nums[low]<nums[high]-n+1){
                low++;
            }
            ans=max(ans,high-low+1);
            high++;
        }
        return n-ans;
    }
};
// @lc code=end

