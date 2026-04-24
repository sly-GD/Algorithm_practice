/*
 * @lc app=leetcode.cn id=1493 lang=cpp
 *
 * [1493] 删掉一个元素以后全为 1 的最长子数组
 */
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = 0;
        int ans = 0;
        int cnt = 0; //记录1的个数
        while (right < n) {
            if (nums[right] == 0) {
                cnt++;
            }
            while (cnt > 1) {
                if (nums[left] == 0) {
                    cnt--;
                }
                left++;
            }
            ans = max(ans, right - left + 1 - cnt);
            right++;
        }
        if(cnt==0){
            ans-=1;
        }
        return ans;
    }
};
// @lc code=end

int main(){
    Solution s;
    vector<int> nums = {1,1,1};
    cout << s.longestSubarray(nums) << endl;
    return 0;
}