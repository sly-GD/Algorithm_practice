/*
 * @lc app=leetcode.cn id=1358 lang=cpp
 *
 * [1358] 包含所有三种字符的子字符串数目
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int numberOfSubstrings(string s) {
        const int n = s.size();
        int res=0;
        int x[3]={0};
        int high =0 ,low = 0;
        while(high<n){
            x[s[high]-'a']++;
            while(x[0] && x[1] && x[2]){
                res+=n-high;
                x[s[low]-'a']--;
                low++;                
            }
            high++;
        }
        return res;
    }
};
// @lc code=end

