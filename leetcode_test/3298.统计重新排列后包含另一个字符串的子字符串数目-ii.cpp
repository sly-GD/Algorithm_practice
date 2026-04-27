/*
 * @lc app=leetcode.cn id=3298 lang=cpp
 *
 * [3298] 统计重新排列后包含另一个字符串的子字符串数目 II
 */
#include <string>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        int cnt1[26]={0},cnt2[26]={0};
        long long ans=0;
        int n=word1.size(),m=word2.size();
        if(m>n)return 0;
        int required=0;
        for(int i=0;i<m;i++){
            cnt2[word2[i]-'a']++;
        }
        for(int i=0;i<26;i++)if(cnt2[i])required++;
        // auto check=[&](int x[],int y[])->bool{
        //     for(int i=0;i<26;i++){
        //         if(cnt1[i]<cnt2[i]){
        //             return false;
        //         }
        //     }
        //     return true;
        // };
        int high=0,low=0,formed=0;
        while(high<n){
            cnt1[word1[high]-'a']++;
            if(cnt1[word1[high]-'a']==cnt2[word1[high]-'a'])formed++;
            while(formed==required){
                //cout<<"high="<<high<<" low="<<low<<endl;
                ans+=n-high;
                
                if(cnt1[word1[low]-'a']==cnt2[word1[low]-'a'])formed--;
                cnt1[word1[low]-'a']--;
                low++;
            }
            high++;
        }
        return ans;
    }
};
// @lc code=end

