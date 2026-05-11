/*
 * @lc app=leetcode.cn id=167 lang=cpp
 *
 * [167] 两数之和 II - 输入有序数组
 */

#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        const int n=numbers.size();
        int l=0,r=n-1;
        while(l<r){
            if(numbers[l]+numbers[r]==target)
                return {l+1,r+1};
            else if(numbers[l]+numbers[r]<target)
                l++;
            else
                r--;
        }
        return {};
    }
};
// @lc code=end

