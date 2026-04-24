/*
 * @lc app=leetcode.cn id=1234 lang=cpp
 *
 * [1234] 替换子串得到平衡字符串
 */
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution {
public:
    // bool test(vector<int> cnt,int n){
    //     for(int i=0;i<26;i++){
    //         if(cnt[i]>n/4)return false;
    //     }
    //     return true;
    // }
    int balancedString(string s) {
        const int n = s.size(),Q=16,W=22,E=4,R=17,target=n/4;
        int cnt[26]={0};
        for(char c:s)cnt[c-'A']++;

        if(cnt[Q]<=target && cnt[E]<=target && cnt[W]<=target && cnt[R]<=target)return 0;
        int high=0,low=0;
        int res = n;
        while(high<n){
            cnt[s[high]-'A']--;
            while(                
                cnt['Q'-'A'] <= target && 
                cnt['W'-'A'] <= target && 
                cnt['E'-'A'] <= target && 
                cnt['R'-'A'] <= target){
                res = min(res,high-low+1);
                cnt[s[low]-'A']++;
                low++;
            }
            high++;
        }
        return res;
    }
};
// @lc code=end

