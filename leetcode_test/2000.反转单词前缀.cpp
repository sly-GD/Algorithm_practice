/*
 * @lc app=leetcode.cn id=2000 lang=cpp
 *
 * [2000] 反转单词前缀
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    string reversePrefix(string word, char ch) {
        for(int i=0;i<word.size();i++){
            if(word[i]==ch){
                reverse(word.begin(),word.begin()+i+1);
                break;
            }
        }
        return word;
    }
};
// @lc code=end

