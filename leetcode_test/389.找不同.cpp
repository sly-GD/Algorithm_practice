/*
 * @lc app=leetcode.cn id=389 lang=cpp
 *
 * [389] 找不同
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    char findTheDifference(string s, string t) {
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        for(int i=0;i<s.size();i++){
            if(s[i]!=t[i]) return t[i];
        }
        return t[t.size()-1];
    }
};
// @lc code=end

