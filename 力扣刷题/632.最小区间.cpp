/*
 * @lc app=leetcode.cn id=632 lang=cpp
 *
 * [632] 最小区间
 */
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        priority_queue<
            tuple<int,int,int>,
            vector<tuple<int,int,int>>,
            greater<tuple<int,int,int>>
        > pq;
        int k= nums.size();
        int maxv = INT_MIN;
        for(int i=0;i<k;i++){
            pq.push({nums[i][0],i,0});
            maxv = max(maxv,nums[i][0]);
        }
        vector<int> ans = {get<0>(pq.top()),maxv};
        while(true){
            auto [val,row,col] = pq.top();
            pq.pop();
            if(maxv - val < ans[1] - ans[0]){
                ans[0] = val;
                ans[1] = maxv;
            }
            if(col == nums[row].size()-1){
                break;
            }
            col++;
            pq.emplace(nums[row][col],row,col);
            maxv = max(maxv,nums[row][col]);

        }
        return ans;
    }
};


// @lc code=end

