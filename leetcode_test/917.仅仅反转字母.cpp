/*
 * @lc app=leetcode.cn id=917 lang=cpp
 *
 * [917] 仅仅反转字母
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    string reverseOnlyLetters(string s) {
        const int n=s.size();
        int l=0,r=n-1;
        while(l<r){
            if(!isalpha(s[l]))l++;
            else if(!isalpha(s[r]))r--;
            else{
                swap(s[l],s[r]);
                l++;
                r--;
            }
        }
        return s;
    }
};
// @lc code=end

