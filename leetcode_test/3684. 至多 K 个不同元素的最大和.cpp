/*
 * @lc app=leetcode.cn id=3684 lang=cpp
 *
 * [3684] 至多 K 个不同元素的最大和
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    vector<int> maxKDistinct(vector<int>& nums, int k) {
        int n=nums.size();
        sort(nums.begin(),nums.end(),greater());
        nums.erase(unique(nums.begin(),nums.end()),nums.end()); //原地去重。unique将相邻重复元素移到末尾，并返回重复元素起始的迭代器
        if(nums.size()>k){
            nums.resize(k);
        }
        return nums;
    }
    vector<int> maxKDistinct_01(vector<int>& nums, int k) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        unordered_map<int,int> x;
        vector<int> ans;
        for(int i=n-1;ans.size()<k&& i>=0;i--){
            int tem=++x[nums[i]];
            if(tem==1){
                ans.push_back(nums[i]);
            }
        }
        return ans;
    }
};
// @lc code=end

