/*
 * @lc app=leetcode.cn id=3090 lang=cpp
 *
 * [3090] 每个字符最多出现两次的最长子字符串
 */

// @lc code=start
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;
class Solution {
public:
    int maximumLengthSubstring(string s) {
        int n = s.size();
        int low=0, high=0;
        unordered_map<char, int> mp;
        int res = 0;
        while(high<n){
            mp[s[high]]++;
            while(mp[s[high]]>2){
                mp[s[low]]--;
                low++;
            }
            res = max(res, high-low+1);
            high++;
        }
        return res;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout << s.maximumLengthSubstring("aaaa");
    return 0;
}