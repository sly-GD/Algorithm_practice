/*
 * @lc app=leetcode.cn id=1610 lang=cpp
 *
 * [1610] 可见点的最大数目
 */

#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <numbers>
using namespace std;
// @lc code=start
#define M_PI 3.14159265358979323846
class Solution {
public:
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        int n = points.size();
        vector<double> d;
        int seam=0,maxx=0;
        for(int i=0;i<n;i++){
            int dx=points[i][0],dy=points[i][1];
            if(dx==location[0] && dy==location[1])seam++;
            else{
                d.emplace_back(atan2(dy-location[1],dx-location[0]));
            }
        }

        sort(d.begin(),d.end());
        int sz=d.size();
        for(int i=0;i<sz;i++)d.emplace_back(d[i]+2*M_PI);

        double angleDegree = angle*M_PI/180;
        for(int i=0,j=0;i<sz;i++){
            while(j+1<=2*sz && d[j+1]-d[i]<=angleDegree){
                j++;
            }
            maxx=max(maxx,j-i+1);
        }
        return maxx+seam;
    }
};
// @lc code=end

