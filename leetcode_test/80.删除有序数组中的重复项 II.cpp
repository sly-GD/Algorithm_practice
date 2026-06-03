/*
 * @lc app=leetcode.cn id=80 lang=cpp
 *
 * [80] 删除有序数组中的重复项 II
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.empty()) return 0;
        int n=nums.size();
        if(n<=2) return n;
        int slow=2;
        for(int fast=2;fast<nums.size();++fast){
            if(nums[fast]!=nums[slow-2]){
                nums[slow++]=nums[fast];
            }
        }
        return slow;
    }
};
// @lc code=end

