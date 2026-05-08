/*
 * @lc app=leetcode.cn id=151 lang=cpp
 *
 * [151] 反转字符串中的单词
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    string reverseWords(string s) {
        const int n=s.size();
        reverse(s.begin(),s.end());
        for(int i=0;i<n;){
            if(s[i]!=' '){
                int j=i++;
                while(i<n && s[i]!=' '){
                    i++;
                }
                reverse(s.begin()+j,s.begin()+i);
            }else{
                i++;
            }
        }int l=0,r=0;
        while(r<n){
            while(r<n && s[r]==' ')r++;
            while(r<n && s[r]!=' ')s[l++]=s[r++];
            while(r<n && s[r]==' ')r++;
            if(r<n)s[l++]=' ';
        }
        s.resize(l);
        return s;
    }
};
// @lc code=end
int main(){
    Solution s;
    cout<<s.reverseWords("  hello world  ")<<endl;
    return 0;
}
