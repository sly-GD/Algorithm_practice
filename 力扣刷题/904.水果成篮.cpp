/*
 * @lc app=leetcode.cn id=904 lang=cpp
 *
 * [904] 水果成篮
 */
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>
using namespace std;
// @lc code=start
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();
        int res = 0;
        unordered_map<int, int> cnt;
        int high =0 , low = 0;
        while(high<n){
            cnt[fruits[high]]++;
            while(cnt.size()>2){
                cnt[fruits[low]]--;
                if(cnt[fruits[low]]==0){
                    cnt.erase(fruits[low]);
                }
                low++;
            }
            res = max(res, high-low+1);
            high++;
        }
        return res;
    }
};
// @lc code=end

