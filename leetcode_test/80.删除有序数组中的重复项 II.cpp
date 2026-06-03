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
        int n=nums.size();
        if(n==1)return n;
        int stack_size=2; //默认前两个元素保留
        for(int i=2;i<n;i++){
            if(nums[i]!= nums[stack_size-2])
                nums[stack_size++]=nums[i];
        }
        return min(stack_size,n);
    }
};
// @lc code=end

