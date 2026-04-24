/*
 * @lc app=leetcode.cn id=1658 lang=cpp
 *
 * [1658] 将 x 减到 0 的最小操作数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int n = nums.size();
        long long sum = 0;
        for(int i=0;i<n;i++){
            sum+=nums[i];
        }
        if(sum<x){
            return -1;
        }
        if(sum == x){
            return n;
        }
        long long target = sum-x;
        int left=0,right=0;
        int maxLen=0;
        long long total=0;
        while(right<n){
            total+=nums[right];
            while(total>target){
                total-=nums[left];
                left++;
            }
            if(total==target){
                maxLen = max(maxLen,right-left+1);
            }
            right++;
        }
        return maxLen==0?-1:n-maxLen;
    }
};
// @lc code=end

