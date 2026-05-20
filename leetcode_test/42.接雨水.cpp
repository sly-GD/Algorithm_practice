/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    //双指针
    int trap_001(vector<int>& height) {
        int n=height.size();
        if(n==0) return 0;
        int res=0,l_max=0,r_max=0;
        int l=0,r=n-1;
        while(l<=r){
            l_max=max(l_max,height[l]);
            r_max=max(r_max,height[r]);

            if(l_max<r_max){
                res+=l_max-height[l];
                l++;
            }else{
                res+=r_max-height[r];
                r--;
            }
        }
        return res;
    }

    //前后缀
    int trap(vector<int>& height) {
        int n=height.size();
        if(n==0) return 0;
        int res=0,l_max=0,r_max=0;
        int l=0,r=n-1;
        vector<int> l_maxs(n),r_maxs(n);
        for(int i=0;i<n;i++){
            l_maxs[i]=max(l_max,height[i]);
            l_max=max(l_max,l_maxs[i]);
        }
        for(int i=n-1;i>=0;i--){
            r_maxs[i]=max(r_max,height[i]);
            r_max=max(r_max,r_maxs[i]);
        }
        for(int i=0;i<n;i++){
            res+=min(l_maxs[i],r_maxs[i])-height[i];
        }

        // while(l<=r){
        //     l_max=max(l_max,height[l]);
        //     r_max=max(r_max,height[r]);

        //     if(l_max<r_max){
        //         res+=l_max-height[l];
        //         l++;
        //     }else{
        //         res+=r_max-height[r];
        //         r--;
        //     }
        // }
        return res;
    }
};
// @lc code=end

