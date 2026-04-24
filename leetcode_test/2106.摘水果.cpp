/*
 * @lc app=leetcode.cn id=2106 lang=cpp
 *
 * [2106] 摘水果
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
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int n = fruits.size();
        long long sum=0;
        int low = std::ranges::lower_bound(fruits,startPos - k , {},[](auto& f) {return f[0];}) - fruits.begin();
        int high = low ;
        for(;high<n && fruits[high][0]<=startPos;high++){
            sum+=fruits[high][1];
        }
        int ans = sum;
        for(;high<n && fruits[high][0]<=startPos+k;high++){
            sum+=fruits[high][1];
            while((fruits[high][0]-startPos)*2 + startPos - fruits[low][0] > k && fruits[high][0] - startPos + (startPos-fruits[low][0])*2 > k){
                sum -= fruits[low][1];
                low++;
            }
            ans = max(ans,(int)sum);
        }
        return ans;
    }
};
// @lc code=end

