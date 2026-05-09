/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    bool isPalindrome(string s) {
        const int n=s.size();
        if(n==0) return true;
        int l=0,r=n-1;
        while(l<r){
            while(l<r && !isalnum(s[l])) l++;
            while(l<r && !isalnum(s[r])) r--;
            if(l<r && tolower(s[l])!=tolower(s[r])) return false;
            l++;r--;
        }
        return true;
    }
};
// @lc code=end

