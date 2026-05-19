/*
 * @lc app=leetcode.cn id=948 lang=cpp
 *
 * [948] 令牌放置
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(),tokens.end());
        int l=0,r=tokens.size()-1;
        int res=0;
        int cur=0;
        while(l<=r){
            cout<<l<<" "<<r<<endl;
            if(power>=tokens[l]){
                power-=tokens[l];
                cur++;
                l++;
                cout<<"z"<<endl;
                res=max(res,cur);
            }
            else{        
                if(cur>0){
                    power+=tokens[r];
                    cur--;
                    r--;
                }else{
                    cout<<"zhel"<<endl;
                    break;
                }
            }
        }
        return res;
    }
};
// @lc code=end

int main(){
    Solution s;
    vector<int> tokens={200,100};
    cout<<s.bagOfTokensScore(tokens,150)<<endl;
    return 0;
}