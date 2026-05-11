/*
 * @lc app=leetcode.cn id=16 lang=cpp
 *
 * [16] 最接近的三数之和
 */

#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        const int n=nums.size();
        sort(nums.begin(),nums.end());
        int ans=nums[0]+nums[1]+nums[2];
        for(int i=0;i<n-2;i++){
            
            int l=i+1,r=n-1;
            while(l<r){
                int sum=nums[i]+nums[l]+nums[r];
                if(abs(sum-target)<abs(ans-target)){
                    ans=sum;
                }
                if(sum<target){
                    l++;
                }else if(sum>target){
                    r--;
                }else{
                    return target;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

