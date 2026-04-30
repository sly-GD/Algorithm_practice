/*
 * @lc app=leetcode.cn id=1156 lang=cpp
 *
 * [1156] 单字符重复子串的最大长度
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int maxRepOpt1(string text) {
        int ans=0,cnt=0;
        const int n=text.size(); 
        int x[26]={0}; 
        vector<pair<int,int>> a;  
        for(int i=0;i<n;i++){
            cnt++;
            if(i<n-1&&text[i]!=text[i+1]){
                a.push_back({text[i]-'a',cnt});
                cnt=0;
            }
            x[text[i]-'a']++;
        }
        a.push_back({text.back()-'a',cnt});
        // for(int i=0;i<a.size();i++){
        //     cout<<a[i].first<<" "<<a[i].
        //     second<<endl;
        //     //cout<<"x "<<x[i]<<endl;
        // }
        for(int i=0;i<a.size();i++){
            int d=0,t=0;
            if(a[i].second<x[a[i].first]) d=a[i].second+1;
            else d=a[i].second;
            if(i+2<a.size()&&a[i].first==a[i+2].first&&a[i+1].second==1&&a[i].second+a[i+2].second<=x[a[i].first]) {
                t=min(a[i].second + a[i+2].second+1,x[a[i].first]);
                //cout<<"fd"<<endl;
            }
            ans=max(ans,max(d,t));
        }
        return ans;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.maxRepOpt1("aaabaaa")<<endl;
    cout<<s.maxRepOpt1("abcdef")<<endl;
    cout<<s.maxRepOpt1("aaaaa")<<endl;
    cout<<s.maxRepOpt1("ababa")<<endl;
    cout<<s.maxRepOpt1("aaabbaaa")<<endl;
    return 0;
}