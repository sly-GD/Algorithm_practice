/*
 * @lc app=leetcode.cn id=3258 lang=cpp
 *
 * [3258] 统计满足 K 约束的子字符串数量 I
 */
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        const int n=s.size();
        int ans=0,cnt1=0,cnt0=0;
        int high=0,low=0;
        while(high<n){
            // if(s[high]=='0'){
            //     cnt0++;
            // }else{
            //     cnt1++;
            // }
            s[high]=='0'?cnt0++:cnt1++;
            while(cnt1>k && cnt0>k){
                // if(s[low]=='0'){
                //     cnt0--;
                // }else{
                //     cnt1--;
                // }
                s[low]=='0'?cnt0--:cnt1--;
                low++;
            }
            ans+=high-low+1;
            //cout<<"high="<<high<<"low="<<low<<"ans="<<ans<<endl;
            high++;
        }
        return ans;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.countKConstraintSubstrings("10101",1)<<endl;
    return 0;
}