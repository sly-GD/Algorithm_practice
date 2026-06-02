/*
 * @lc app=leetcode.cn id=2122 lang=cpp
 *
 * [2122] 还原原数组
 */
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> recoverArray(vector<int>& nums) {
        int n=nums.size(); 
        sort(nums.begin(),nums.end());
        for(int i=1;i<n;i++){
            if(nums[i]==nums[i-1])continue;
            int d=nums[i]-nums[0];
            if(d <= 0 || d%2!=0)continue; //k必须是整数
            int k=d/2;
            vector<bool> vis(n,false);
            vector<int> ans;
            //vis[0]=true;
            for(int l=0,r=1;l<n;){
                if(vis[l]){
                    l++;
                    continue;
                }
                while(r<n && (vis[r] || nums[r]<nums[l]+2*k)){
                    r++;
                }
                if(r>=n || nums[r] != nums[l]+2*k) break;
                vis[l]=true;vis[r]=true;
                ans.push_back(nums[l]+k);
                l++;r++;
            }

            if(ans.size()==n/2)return ans;

        }
        return {};
    }
};
// @lc code=end

