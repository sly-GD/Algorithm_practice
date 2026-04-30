/*
 * @lc app=leetcode.cn id=3794 lang=cpp
 *
 * [3794] 反转字符串前缀
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    string reversePrefix(string s, int k) {
        for(int i=0;i<k/2;i++){
            swap(s[i],s[k-i-1]);
        }
        return s;
    }
};
// @lc code=end

