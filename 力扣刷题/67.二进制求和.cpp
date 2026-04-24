/*
 * @lc app=leetcode.cn id=67 lang=cpp
 *
 * [67] 二进制求和
 */
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution {
public:
    string addBinary(string a, string b) {
        int n = max(a.size(),b.size());
        string ans;
        ans.reserve(n);
        int i = a.size() - 1, j = b.size() - 1, carry = 0;
        while(i>=0 || j>= 0 ||carry>0){
            int x=(i>=0)?a[i--]-'0':0;
            int y=(j>=0)?b[j--]-'0':0;
            int c = x + y + carry;
            ans.push_back((c%2)+'0');//ASCLL码转换成字符。常用！！将单个int 转换为char
            carry = c/2;
            //cout<<carry<<' '<<ans<<endl;
        }
        //cout<<carry<<" 123 "<<ans<<endl;
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.addBinary("11","1")<<endl;
    return 0;
}