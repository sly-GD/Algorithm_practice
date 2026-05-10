/*
 * @lc app=leetcode.cn id=1471 lang=cpp
 *
 * [1471] 数组中的 k 个最强值
 */

#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    vector<int> getStrongest(vector<int>& arr, int k) {
        const int n=arr.size();
        sort(arr.begin(),arr.end());
        int mid = arr[(n-1)/2];
        int l=0,r=n-1;
        vector<int> ans;
        while(k--){
            if(abs(arr[r]-mid)>=abs(arr[l]-mid)){
                ans.push_back(arr[r--]);
            }else{
                ans.push_back(arr[l++]);
            }
        }
        return ans;
    }
};
// @lc code=end

