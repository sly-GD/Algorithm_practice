/*
 * @lc app=leetcode.cn id=345 lang=cpp
 *
 * [345] 反转字符串中的元音字母
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    string reverseVowels(string s) {
        string vowels="aeiouAEIOU";
        int l = 0, r = s.size() - 1;
        while (l < r) {
            while(l<r&&vowels.find(s[l]) == string::npos) {
                l++;
            }
            while(l<r&&vowels.find(s[r])==string::npos)r--;
            swap(s[r],s[l]);
            cout<<s<<endl;
            l++;
            r--;
        }
        return s;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.reverseVowels("lceCreAm")<<endl;
    return 0;
}