/*
 * @lc app=leetcode.cn id=1574 lang=cpp
 *
 * [1574] 删除最短的子数组使剩余数组有序
 */
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n=arr.size();
        int ans=0;
        int l=0,r=n-1;
        while(r && arr[r-1]<=arr[r]){
            --r;
        }
        if(r==0)return 0;
        ans=r;
        for(;l==0 || arr[l-1]<=arr[l];++l){
            while(r<n && arr[r]<arr[l]){
                ++r;
            }
            ans=min(ans,r-l-1);
        }
        return ans;
    }
};
// @lc code=end

