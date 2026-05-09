/*
 * @lc app=leetcode.cn id=1750 lang=cpp
 *
 * [1750] 删除字符串两端相同字符后的最短长度
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int minimumLength(string s) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        const int n=s.size();
        int l=0,r=n-1;
        while(l<r){
            if(s[l]!=s[r]){
                break;
            }
            while(l+1<r && s[l]==s[l+1])l++;
            while(l<r-1 && s[r]==s[r-1])r--;
            l++,r--;
            //cout<<l<<" "<<r<<endl;
        }//cout<<l<<" "<<r<<endl;
        return r-l+1;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.minimumLength("aabccabba")<<endl;
    return 0;
}