/*
 * @lc app=leetcode.cn id=541 lang=cpp
 *
 * [541] 反转字符串 II
 */

#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    string reverseStr(string s, int k) {
        for (int i=0;i<s.size();i+=2*k){
            if (i+k<=s.size()){
                reverse(s.begin()+i,s.begin()+i+k);
            }
            else{
                reverse(s.begin()+i,s.end());
            }
        }
        return s;
    }
};
// @lc code=end

