/*
 * @lc app=leetcode.cn id=424 lang=cpp
 *
 * [424] 替换后的最长重复字符
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int characterReplacement(string s, int k) {
        const int n = s.size();
        int left=0,right=0;
        int maxf=0,temp=0;
        int cnt[26]={0};
        while(right<n){
            cnt[s[right]-'A']++;
            temp = max(temp, cnt[s[right]-'A']);
            if(right-left+1-temp>k){
                cnt[s[left++]-'A']--;
            }
            maxf = max(maxf,right-left+1);
            right++;
        }
        return maxf;
    }
};
// @lc code=end

