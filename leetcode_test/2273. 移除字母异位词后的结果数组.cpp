/*
 * @lc app=leetcode.cn id=2273 lang=cpp
 *
 * [2273] 移除字母异位词后的结果数组
 */
#include <bits/stdc++.h> 
using namespace std;
class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        int n=words.size();
        int k=0;
        string base="";
        for(auto& word:words){
            string s=word;
            //std::ranges::sort(s);
            std::sort(s.begin(), s.end());
            if(s!=base){
                base=move(s); //浅拷贝
                words[k++]=word;
            }
        }
        words.resize(k);
        return words;  

    }
};
 // @lc code=end

