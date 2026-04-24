/*
 * @lc app=leetcode.cn id=3325 lang=cpp
 *
 * [3325] 字符至少出现 K 次的子字符串 I
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int numberOfSubstrings(string s, int k) {
        const int n = s.size();
        int res=0;
        int high=0,low=0;
        int cnt[26]={0};
        while(high<n){
            cnt[s[high]-'a']++;
            while(cnt[s[high]-'a']>=k){
                res+=n-high;
                cnt[s[low]-'a']--;
                low++;
            }
            high++;
        }
        return res;
    }
};
// @lc code=end

