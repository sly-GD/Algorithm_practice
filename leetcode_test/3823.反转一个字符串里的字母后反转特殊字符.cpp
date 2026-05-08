/*
 * @lc app=leetcode.cn id=3823 lang=cpp
 *
 * [3823] 反转一个字符串里的字母后反转特殊字符
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
    inline void reverse(string& s,auto&& f){
        for(int i=0,j=s.size()-1;i<j;i++,j--){
            while(i<j && f(s[i])){
                i++;
            }
            while(i<j && f(s[j])){
                j--;
            }
            swap(s[i],s[j]);
        }
    }   
public:
    string reverseByType(string s) {
        reverse(s,::isalpha);
        reverse(s,[](char ch){return !isalpha(ch);});
        return s;
    }
};
// @lc code=end

