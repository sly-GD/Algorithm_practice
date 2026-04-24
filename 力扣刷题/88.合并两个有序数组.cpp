/*
 * @lc app=leetcode.cn id=88 lang=cpp
 *
 * [88] 合并两个有序数组
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // for(int i=0;i<n;i++){
        //     nums1[m+i]=nums2[i];
        // }
        // sort(nums1.begin(),nums1.end());
        int p1=m-1,p2=n-1,p=m+n-1;
        while(p2>=0){
            if(p1>=0 && nums1[p1]>nums2[p2])
                nums1[p--]=nums1[p1--];
            else
                nums1[p--]=nums2[p2--];
        }
    }
};
// @lc code=end

