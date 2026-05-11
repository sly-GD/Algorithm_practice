/*
 * @lc app=leetcode.cn id=633 lang=cpp
 *
 * [633] 平方数之和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    bool judgeSquareSum(int c) {
        long long l=0,r=sqrt(c);
        long long l2=0,r2=r*r;
        while(l<=r){
            long long sum=l2+r2;
            //cout<<sum<<endl;
            if(sum==c) return true;
            else if(sum<c){
                l++;
                l2+=2*l-1;
            }else{
                r--;
                r2-=2*r+1;
            }
        }
        return false;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.judgeSquareSum(5)<<endl;
    cout<<s.judgeSquareSum(2147482647)<<endl;
    return 0;
}