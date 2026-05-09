/*
 * @lc app=leetcode.cn id=2105 lang=cpp
 *
 * [2105] 给植物浇水 II
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int l=0,r=plants.size()-1;
        int a=capacityA,b=capacityB;
        int ans=0;
        while(l<r){
            if(a<plants[l]){
                ans++;
                a=capacityA;
            }
            a-=plants[l++];
            if(b<plants[r]){
                ans++;
                b=capacityB;
            }
            b-=plants[r--];
            if(l==r){
                if(a<plants[l]&& b<plants[r])ans++;
            }
        }
        return ans;
    }
};
// @lc code=end

