/*
 * @lc app=leetcode.cn id=3775 lang=cpp
 *
 * [3775] 反转元音数相同的单词
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
    static inline const string VOWELS = "aeiou";

    template<ranges::input_range R>
    int count_vowel(const R& s){
        int vowel=0;
        for(char c: s){
            if(VOWELS.find(c) != string::npos){
                vowel++;
            }
        }
        return vowel;
    }
public:
    string reverseWords(string s) {
        const int n=s.size();
        int cnt0=-1;
        for(auto&& t:s | std::views::split(' ')){
            int cnt = count_vowel(t);
            if(cnt0<0){
                cnt0=cnt;
            }else if(cnt0==cnt){
                ranges::reverse(t);
            }
        }
        return s;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.reverseWords("aebc daed")<<endl;
    cout<<s.reverseWords("banana healthy")<<endl;
    cout<<s.reverseWords("a")<<endl;
    cout<<s.reverseWords("cat and mice")<<endl;

    return 0;
}