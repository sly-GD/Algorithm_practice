/*
 * @lc app=leetcode.cn id=2200 lang=cpp
 *
 * [2200] 找出数组中的所有 K 近邻下标
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        int n=nums.size();
        int r=0,l=0;
        vector<int> ans;
        while(r<n){
            if(nums[r]!=key){r++;continue;}
            l=max(l,r-k);
            while(l<=min(r+k,n-1))
                ans.push_back(l++);
            r++;
        }
        return ans;
    }
};
// @lc code=end

