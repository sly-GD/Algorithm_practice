/*
 * @lc app=leetcode.cn id=1712 lang=cpp
 *
 * [1712] 将数组分成三个子数组的方案数
 */
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")

class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        const int MOD=1e9+7,n=nums.size();
        long long maxf=0,sum[n+1];
        sum[0]=0;
        for(int i =0;i<n;i++) sum[i+1]=sum[i]+nums[i];
        for(int r=2;r<n && 3*sum[r]<=2*sum[n];r++){
            int i = lower_bound(sum+1,sum+r,2*sum[r]-sum[n])-sum;
            int j = upper_bound(sum+i,sum+r,sum[r]/2)-sum;
            maxf=(maxf+j-i)%MOD;
        }

        return (int)maxf;
    }
};
// @lc code=end

