/*
 * @lc app=leetcode.cn id=1616 lang=cpp
 *
 * [1616] 分割两个字符串得到回文串
 */
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
    inline bool isPalindrome(string s){
        int n = s.size();
        for(int i = 0; i < n / 2; i++){
            if(s[i] != s[n - i - 1]) return false;
        }
        return true;
    }

    inline bool check(string& a,string& b){
        int n = a.size();
        int l=0,r=n-1;
        while(l<r && a[l]==b[r]){
            l++;r--;
        }
        return isPalindrome(a.substr(l,r-l+1)) || isPalindrome(b.substr(l,r-l+1));
    }

public:
    bool checkPalindromeFormation(string a, string b) {
        return check(a,b)||check(b,a);
    }
};
// @lc code=end
int main(){
    Solution s;
    cout<<s.checkPalindromeFormation("xbdef", "xecab")<<endl;
    cout<<s.checkPalindromeFormation("ulacfd", "jizalu")<<endl;
    return 0;
}
