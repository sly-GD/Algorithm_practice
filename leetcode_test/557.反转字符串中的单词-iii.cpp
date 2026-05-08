/*
 * @lc app=leetcode.cn id=557 lang=cpp
 *
 * [557] 反转字符串中的单词 III
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    string reverseWords(string s) {
        for(int i=0,start=0;i<s.size();i++){
            if(s[i]==' '){
                reverse(s.begin()+start,s.begin()+i);
                start=i+1;
            }
        }
        int j=s.size()-1;
        while(j>=0&&s[j]!=' ')j--;
        reverse(s.begin()+j+1,s.end());
        return s;
    }
};
// @lc code=end

