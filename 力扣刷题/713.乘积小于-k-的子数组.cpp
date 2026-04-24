/*
 * @lc app=leetcode.cn id=713 lang=cpp
 *
 * [713] 乘积小于 K 的子数组
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if(k<=1)return 0;
        int n = nums.size();
        int res=0;
        int high=0,low=0;
        long long sum=1;
        //sort(nums.begin(),nums.end());
        while(high<n){
            sum*=nums[high];
            while(sum>=k){
                sum/=nums[low];
                low++;
            }
            res+=high-low+1;
            high++;
        }
        return res;
    }
};
// @lc code=end

