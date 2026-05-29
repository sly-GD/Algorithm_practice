/*
 * @lc app=leetcode.cn id=2972 lang=cpp
 *
 * [2972] 统计移除递增子数组的数目 II
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution {
public:
    long long incremovableSubarrayCount(vector<int>& nums) {
        int n=nums.size();
        long long ans=0;
        int left=0,right=n-1;
        while(left<n-1){
            if(nums[left]>=nums[left+1])break;
            left++;
        }
        while(right>0){
            if(nums[right]<=nums[right-1])break;
            right--;
        }
        if(left==n-1){
            return (long long)n*(n+1)/2;
        }
        int j=right;
        for(int i=0;i<=left;++i){
            
            while(j<n && nums[i]>=nums[j])j++;
            ans+=(long long)n-j;
        }
        return ans+(long long)(n-right)+(long long)(left+1)+1; //+1是删除整个数组
    }
};
// @lc code=end

