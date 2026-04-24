/*
 * @lc app=leetcode.cn id=2730 lang=cpp
 *
 * [2730] 找到最长的半重复子字符串
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int longestSemiRepetitiveSubstring(string s) {
        int n = s.size();
        if(n==1)return 1;
        int ans = 0;
        int high = 1,low = 0;
        int f=0;
        while(high<n){
            if(s[high]==s[high-1]){
                f+=1;
            }
            while(f>1){
                if(s[low]==s[low+1]){
                    f-=1;
                }
                low+=1;
            }
            ans = max(ans,high-low+1);
            high+=1;
        }
        return ans;
    }
};
// @lc code=end

