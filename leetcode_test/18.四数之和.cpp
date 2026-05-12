/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int n=nums.size();
        for(int i=0;i<n-3;i++){
            if(i>0&&nums[i]==nums[i-1]) continue;
            long long y=nums[i];
            if(y+nums[i+1]+nums[i+2]+nums[i+3]>target) break;
            if(y+nums[n-3]+nums[n-2]+nums[n-1]<target) continue;

            
            for(int j=i+1;j<n-2;j++){
                if(j>i+1&&nums[j]==nums[j-1]) continue;
                long long x=nums[j];
                if(y+x+nums[j+1]+nums[j+2]>target) break;
                if(y+x+nums[n-2]+nums[n-1]<target) continue;
                int l=j+1,r=n-1;
                while(l<r){
                    long long sum=x+y+nums[l]+nums[r];
                    if(sum==target){
                        res.push_back({(int)x,(int)y,nums[l],nums[r]});
                        while(l<r&&nums[l]==nums[l+1]) l++;
                        while(l<r&&nums[r]==nums[r-1]) r--;
                        l++;
                        r--;
                    }
                    else if(sum<target) l++;
                    else r--;
                }
            }
        }
        return res;
    }
};
// @lc code=end

