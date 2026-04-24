/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 找出字符串中第一个匹配项的下标
 */
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty()) return 0;
        int n = haystack.size(), m = needle.size();
        vector<int> next_arr(m);
        fill(next_arr.begin(),next_arr.end(),0);
        for (int i =1,j=0;i<m;i++){
            while(j>0 && needle[i]!=needle[j]){
                j=next_arr[j-1];
            }
            if(needle[i]==needle[j]){
                j++;
                next_arr[i]=j;
            }
        }
        for(int i=0,j=0;i<n;i++){
            while(j>0 && haystack[i]!=needle[j]){
                j=next_arr[j-1];
            }
            if(haystack[i]==needle[j]){
                j++;
            }
            if(j==m){
                return i-m+1;
            }
        }
        return -1;
    }
};
// @lc code=end

