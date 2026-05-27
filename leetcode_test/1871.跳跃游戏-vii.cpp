/*
 * @lc app=leetcode.cn id=1871 lang=cpp
 *
 * [1871] 跳跃游戏 VII
 */
#include <string>
#include <vector>
using namespace std;
// @lc code=start
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n=s.size();
        //if(s[n-1]=='0') return true;
        vector<bool> can_reaches(n,false);
        can_reaches[0]=true;
        int j=1;
        for(int i=0;i<n&&j<n;i++){
            if(s[i]=='0'&&can_reaches[i]){
                for(j=max(j,i+minJump);j<=min(n-1,i+maxJump);j++){
                    can_reaches[j]=true;}
            }

        }
        return can_reaches[n-1] && s[n-1]=='0';
    }
};
// @lc code=end

