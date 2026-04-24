/*
 * @lc app=leetcode.cn id=2302 lang=cpp
 *
 * [2302] 统计得分小于 K 的子数组数目
 */
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;
// @lc code=start
#pragma optimize("O3")
#pragma target("avx2")
class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        const int n=nums.size();
        long long ans=0;
        int high=0,low=0;
        long long sum=0;
        while(high<n){
            sum+=nums[high];
            while(sum*(high-low+1)>=k){
                sum-=nums[low];
                low++;
            }
            ans+=high-low+1;
            high++;
        }
        return ans;
    }
};
// @lc code=end

