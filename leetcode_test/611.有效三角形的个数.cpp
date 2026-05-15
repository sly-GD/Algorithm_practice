/*
 * @lc app=leetcode.cn id=611 lang=cpp
 *
 * [611] 有效三角形的个数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        int res=0;
        for(int i=n-1;i>1;i--){
            int l=0,r=i-1;
            while(l<r){
                if(nums[i]<nums[l]+nums[r]){
                    res+=r-l;
                    r--;

                }
                else{
                    
                    l++;

                }

            }
        }
        return res;
    }
};
// @lc code=end

