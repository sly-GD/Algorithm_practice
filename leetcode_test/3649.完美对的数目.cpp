/*
 * @lc app=leetcode.cn id=3649 lang=cpp
 *
 * [3649] 完美对的数目
 */
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution {
public:
    long long perfectPairs(vector<int>& nums) {
        int n=nums.size();
        long long ans=0;
        for(int& x:nums)x=abs(x);
        sort(nums.begin(),nums.end());
        int l=0;
        for(int i=0;i<n;i++){
            int  b=nums[i];
            while(l<n&&nums[l]*2<b)l++;

            ans+=i-l;
        }
        return ans;
    }
};
// @lc code=end

