/*
 * @lc app=leetcode.cn id=3306 lang=cpp
 *
 * [3306] 元音辅音字符串计数 II
 */
#include <string>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    long long countOfSubstrings(string word, int k) {
        const int n=word.size();
        auto solve=[&](int goal)->long long{
            long long ans=0;
            //int letter[26]={0};
            int high=0,low=0;
            int cnt[6]={0};
            while(high<n){
                int x=word[high]-'a';
                char c=word[high];
                //letter[x]++;
                if(c=='a') cnt[0]++;
                else if(c=='e') cnt[1]++;
                else if(c=='i') cnt[2]++;
                else if(c=='o') cnt[3]++;
                else if(c=='u') cnt[4]++;
                else cnt[5]++;
                while(cnt[1] && cnt[2] && cnt[3] && cnt[4] && cnt[0] && cnt[5]>=goal){
                    c=word[low];
                    if(c=='a') cnt[0]--;
                    else if(c=='e') cnt[1]--;
                    else if(c=='i') cnt[2]--;
                    else if(c=='o') cnt[3]--;
                    else if(c=='u') cnt[4]--;
                    else cnt[5]--;
                    low++;
                }
                ans+=low;
                high++;
            }
            return ans;
        };

        return solve(k)-solve(k+1);
        }
};
// @lc code=end

