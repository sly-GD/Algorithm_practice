/*
 * @lc app=leetcode.cn id=2563 lang=cpp
 *
 * [2563] 统计公平数对的数目
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:

    //二分查找
    long long countFairPairs_0(vector<int>& nums, int lower, int upper) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        long long ans=0;
        for(int i=0;i<n;i++){
            int l=lower_bound(nums.begin(),nums.begin()+i,lower-nums[i])-nums.begin();
            int r=upper_bound(nums.begin(),nums.begin()+i,upper-nums[i])-nums.begin();
            ans+=r-l;


        }return ans;
    }

    //相向三指针
    long long countFairPairs_01(vector<int>& nums, int lower, int upper) {
        int n=nums.size();
        int l=n,r=n;
        sort(nums.begin(),nums.end());
        long long ans=0;
        for(int i=0;i<n;i++){
            while(l && nums[l-1]+nums[i]>=lower){
                l--;
            }
            while(r && nums[r-1]+nums[i]>upper){
                r--;
            }
            ans+=min(r,i)-min(l,i);


        }return ans;
    }

    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        
        auto count = [&](int upper){
            long long ans=0;
            int l=0,r=n-1;
            while(l<=r){
                if(nums[l]+nums[r]<=upper){
                    ans+=r-l;
                    l++;
                }else{
                    r--;
                }
            }
            return ans;            
        };
        return count(upper)-count(lower-1);

    }
};
// @lc code=end

