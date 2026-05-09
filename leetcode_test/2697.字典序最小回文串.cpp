/*
 * @lc app=leetcode.cn id=2697 lang=cpp
 *
 * [2697] 字典序最小回文串
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    string makeSmallestPalindrome(string s) {
        const int n=s.size();
        int r=n-1,l=0;
        while(l<r){
            char c=min(s[r],s[l]);
            s[l]=c,s[r]=c;
            l++,r--;
        }
        return s;
    }
};
// @lc code=end

