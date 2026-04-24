/*
 * @lc app=leetcode.cn id=2537 lang=cpp
 *
 * [2537] 统计好子数组的数目
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        int n = nums.size();
        long long res=0;
        int cnt=0,high=0,low=0;
        unordered_map<int,int> mp;

        mp.reserve(n);//预分配n个哈希槽，减少计算
        //int x[]
        while(high<n){
            cnt+=mp[nums[high]]++;
            while(cnt>=k){
                res+=n-high;
                cnt-=--mp[nums[low++]];
            }
            high++;
        }
        return res;
    }
};
// @lc code=end

int main(){
    Solution s;
    vector<int> nums = {3,1,4,3,2,2,4};
    cout<<s.countGood(nums,2)<<endl;
    return 0;
}