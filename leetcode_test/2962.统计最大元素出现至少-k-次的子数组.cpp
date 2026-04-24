/*
 * @lc app=leetcode.cn id=2962 lang=cpp
 *
 * [2962] 统计最大元素出现至少 K 次的子数组
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        const int n = nums.size(),maxv=*max_element(nums.begin(),nums.end());
        long long cnt=0,res=0;
        int high=0,low=0;
        while(high<n){
            if(nums[high]==maxv){
                cnt++;
            }
            while(cnt==k){
                res+=n-high;
                if(nums[low]==maxv){
                    cnt--;
                }
                low++;
            }
            high++;
        }
        return res;
    }
};
// @lc code=end

