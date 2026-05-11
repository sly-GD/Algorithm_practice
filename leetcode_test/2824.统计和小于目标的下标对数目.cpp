/*
 * @lc app=leetcode.cn id=2824 lang=cpp
 *
 * [2824] 统计和小于目标的下标对数目
 */

#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        const int n=nums.size();
        int ans=0;
        sort(nums.begin(),nums.end());
        int l=0,r=n-1;
        while(l<r){
            if(nums[l]+nums[r]<target){
                ans+=r-l;
                l++;
            }else{
                r--;
            }
        }
        return ans;
    }
};
// @lc code=end

