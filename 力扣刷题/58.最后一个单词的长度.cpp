/*
 * @lc app=leetcode.cn id=58 lang=cpp
 *
 * [58] 最后一个单词的长度
 */
#include<bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int lengthOfLastWord(string s) {
        int len=0,n=s.size();
        int i=n-1;
        while(i>=0&&s[i]==' ') i--;
        while(i>=0&&s[i]!=' '){
            len++;
            i--;
        }
        return len;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.lengthOfLastWord("Hello World");
    return 0;
}