/*
 * @lc app=leetcode.cn id=825 lang=cpp
 *
 * [825] 适龄的朋友
 */
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        int cnt[121]={0};
        for(auto x:ages)cnt[x]++;
        int ans = 0;
        int curent=0;
        for(int i=0,j=0;i<121;i++){
            //if(cnt[i]==0)continue;
            curent+=cnt[i];
            if(j*2<=i+14){
                curent-=cnt[j];
                j++;
            }
            if(curent>0){
                ans+=curent*cnt[i]-cnt[i];
            }
        }
        return ans;
    }
};
// @lc code=end

int main(){
    Solution s;
    vector<int> ages={16,16},ages1={16,17,18};
    cout<<s.numFriendRequests(ages)<<endl;
    cout<<s.numFriendRequests(ages1)<<endl;
    return 0;
}