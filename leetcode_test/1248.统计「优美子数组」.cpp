/*
 * @lc app=leetcode.cn id=1248 lang=cpp
 *
 * [1248] 统计「优美子数组」
 */
#include <vector>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        const int n=nums.size();
        auto solve=[&](int goal)->int {
            long long ans=0;
            int cnt=0;
            int high=0,low=0;
            while(high<n) {
                (nums[high] & 1)==0?0:++cnt;
                while(cnt>=goal){
                    (nums[low]&1)==0?0:cnt--;
                    ++low;
                }
                ans+=low;
                high++;
            }
            return ans;
        };
        return solve(k)-solve(k+1);
    }
};
// @lc code=end

