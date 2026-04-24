/*
 * @lc app=leetcode.cn id=2904 lang=cpp
 *
 * [2904] 最短且字典序最小的美丽子字符串
 */
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_set>
using namespace std;
// @lc code=start
class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.size();
        int left = 0, right = 0;
        string tp;
        unordered_set<string> st;
        while(right<n){
            tp.append(1,s[right]);
            while(count(tp.begin(),tp.end(),'1')==k){
                st.insert(tp);
                tp.erase(tp.begin());
            }
            right++;
        }

        if(st.empty()){
            return "";
        }

        vector<string> vec(st.begin(),st.end());
        sort(vec.begin(),vec.end(),[](string &a,string &b){
            if(a.size()!=b.size()){
                return a.size()<b.size();
            }
            return a<b;
        });
        return vec[0];
    }
};
// @lc code=end

