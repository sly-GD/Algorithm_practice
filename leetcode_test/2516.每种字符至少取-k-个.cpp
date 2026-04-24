/*
 * @lc app=leetcode.cn id=2516 lang=cpp
 *
 * [2516] 每种字符至少取 K 个
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution
{
public:
    int takeCharacters(string s, int k)
    {
        int n = s.size();
        int cnt[3] = {0};
        int high = 0, low = 0;
        int res = 0;
        for(char c : s)cnt[c - 'a']++;
        if(cnt[0] < k || cnt[1]<k || cnt[2]<k)return -1;
        //int a=cnt[0],b=cnt[1],c=cnt[2];
        //cnt[0]=0,cnt[1]=0,cnt[2]=0;
        //cout<<'a'<<'b'<<'c'<<endl;
        while (high < n){
            cnt[s[high] - 'a']--;
            //cout<<cnt[0]<<' '<<cnt[1]<<' '<<cnt[2]<<endl;
            while (cnt[s[high]-'a']<k)
            {
                cnt[s[low] - 'a']++;
                low++;
            }
            res = max(res, high - low + 1);
            high++;
        }
        return n-res;
    }
};
// @lc code=end

int main(){
    Solution s;
    cout<<s.takeCharacters("aabaaaacaabc",2)<<endl;
    return 0;
}