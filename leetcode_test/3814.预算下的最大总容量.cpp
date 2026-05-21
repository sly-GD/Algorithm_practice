/*
 * @lc app=leetcode.cn id=3814 lang=cpp
 *
 * [3814] 预算下的最大总容量
 */
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxCapacity(vector<int>& costs, vector<int>& capacity, int budget) {
        int n=costs.size();
        vector<pair<int,int>> v;
        for(int i=0;i<n;i++){
            if(costs[i]<budget){
                v.push_back({costs[i],capacity[i]});
            }
        }
        sort(v.begin(),v.end(),[](pair<int,int>a,pair<int,int>b){
        return a.first<b.first;});
        n=v.size();
        int ans=0,l=0;
        vector<int> pre_max(n+1);
        for(int r=n-1;r>=0;r--){
            while(l<r && v[r].first+v[l].first<budget){
                pre_max[l+1]=max(pre_max[l],v[l].second);  
                l++;              
            }
            ans=max(ans,pre_max[min(l,r)]+v[r].second);

        }
        return ans;
    }
};
// @lc code=end

