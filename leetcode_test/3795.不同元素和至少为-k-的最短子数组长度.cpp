/*
 * @lc app=leetcode.cn id=3795 lang=cpp
 *
 * [3795] 不同元素和至少为 K 的最短子数组长度
 */
#include <vector>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    int minLength(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> f(100001, 0);
        int ans = INT_MAX;
        int low = 0,high=0;
        long long sum=0;
        while(high<n){
            //去除窗口重复
            f[nums[high]]++;
            if(f[nums[high]]==1)sum+=nums[high];
            while(sum>=k){
                ans = min(ans, high-low+1);
                f[nums[low]]--;
                if(f[nums[low]]==0)sum-=nums[low];
                low++;
            }
            high++;
        }   
        return ans==INT_MAX?-1:ans;
    }
};
// @lc code=end

