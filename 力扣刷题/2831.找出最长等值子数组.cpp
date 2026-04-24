/*
 * @lc app=leetcode.cn id=2831 lang=cpp
 *
 * [2831] 找出最长等值子数组
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int longestEqualSubarray(vector<int>& nums, int k) {
        int cnt[100001]={0};
        //unordered_map<int,int> mp;
        int ans=0;
        int maxCount =0;
        int high=0,low=0;
        int n=nums.size();
        while(high<n){
            cnt[nums[high]]++;
            maxCount=max(maxCount,cnt[nums[high]]);
            while(high-low+1-maxCount>k){
                //maxCount=maxCount_(mp);
                cnt[nums[low]]--;
                low++;
            }
            //maxCount=maxCount_(mp);
            ans=max(ans,maxCount);
            high++;
        }
        return ans;
    }
};
// @lc code=end

