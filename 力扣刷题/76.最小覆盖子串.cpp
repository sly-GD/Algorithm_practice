/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 */
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution {
public:
    string minWindow(string s, string t) {
        int n=s.size(),m=t.size();
        int kind=0;
        //unordered_map<char,int> need,window;
        int need[128]={0},window[128]={0};
        for(char c:t){
            need[c]++;
            if(need[c]==1)kind++;
        }
        int high=0,low=0,res=0,start=0,temp=INT_MAX;
        while(high<n){
            char c=s[high];
            window[c]++;
            if(window[c]==need[c])res++;
            // if(need.count(c)&&window[c]==need[c])res++;
            while(res==kind){               
                if(temp>high-low+1){
                    start=low;
                    temp=high-low+1;
                }
                if(window[s[low]]==need[s[low]])res--;
                window[s[low]]--;
                low++;
            }
            high++;
        }
        return temp==INT_MAX?"":s.substr(start,temp);
        //return s.substr(y,x-y+1);
    }
};
// @lc code=end

