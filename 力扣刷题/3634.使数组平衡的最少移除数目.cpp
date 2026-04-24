/*
 * @lc app=leetcode.cn id=3634 lang=cpp
 *
 * [3634] 使数组平衡的最少移除数目
 */
#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
        // for(int i=0;i<n;i++){
        //     cout<<nums[i]<<" ";
        // }
        int high = 0,low = 0;
        int res=0;
        while(high<n){
            long long temp=(long long)nums[low]*k;
            while(high<n&&nums[high]<=temp){
                high++;
            }
            res = max(res,high-low);
            low++;
        }
        return n-res;
    }
};
// @lc code=end
int main(){
    Solution s;
    vector<int> nums = {2,1,5};
    cout<<s.minRemoval(nums,2)<<endl;
    return 0;
}
