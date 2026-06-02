/*
 * @lc app=leetcode.cn id=581 lang=cpp
 *
 * [581] 最短无序连续子数组
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n=nums.size();
        if(n<=1)return 0;
        int high=-1,low=0;
        int max_=nums[0],min_=nums[n-1];
        for(int i=0;i<n;i++){
            if(nums[i]>=max_)max_=nums[i];
            else{
                high=i;
            }
        }
        for(int j=n-1;j>=0;j--){
            if(nums[j]<=min_)min_=nums[j];
            else{
                low=j;
            }
        }
        return high==-1 ? 0:high-low+1;
    }
};
// @lc code=end

