/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        int max=0;
        int l=0,r=n-1;
        while(l<r){
            int area=min(height[l],height[r])*(r-l);
            if(area>max){
                max=area;
            }
            if(height[l]<height[r]){
                l++;
            }else{
                r--;
            }
        }
        return max;
    }
};
// @lc code=end

