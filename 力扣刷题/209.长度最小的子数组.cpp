/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int ans = INT_MAX;
        int high=0,low=0;
        long long sum=0;
        bool flag= true;
        while(high<n){
            sum+=nums[high];
            while(sum>=target){
                ans = min(ans,high-low+1);
                flag=false;
                if(ans==1) return ans;
                sum-=nums[low];
                low++;
            }
            high++;
        }
        if(flag)ans=0;
        return ans;
    }
};
// @lc code=end

