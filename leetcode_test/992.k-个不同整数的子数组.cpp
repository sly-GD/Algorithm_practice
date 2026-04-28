/*
 * @lc app=leetcode.cn id=992 lang=cpp
 *
 * [992] K 个不同整数的子数组
 */
#include <vector>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
    inline int solve(vector<int>& nums, int k,int n){
        int ans=0;
        vector<int> cnt(n+1,0);
        int high=0,low=0;
        int x=0;
        while(high<n){
            cnt[nums[high]]++==0?x++:0;
            while(x>=k){
                --cnt[nums[low]]==0?x--:0;
                low++;
            }
            ans+=low;
            high++;
        }
        return ans;
    }
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        int n=nums.size();
        return solve(nums,k,n)-solve(nums,k+1,n);
    }
};
// @lc code=end

