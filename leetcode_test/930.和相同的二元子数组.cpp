/*
 * @lc app=leetcode.cn id=930 lang=cpp
 *
 * [930] 和相同的二元子数组
 */
#include <vector>
#include <iostream>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        const int n=nums.size();
        using ll=long long;
        auto solve=[&](int target)->ll{
            int high=0,low=0;
            int sum=0;
            ll ans=0;
            while(high<n){
                sum+=nums[high];
                while(low<=high&&sum>=target){
                    sum-=nums[low];
                    low++;
                    cout<<"low++"<<endl;
                }
                ans+=low;
                cout<<"ans="<<ans<<" low="<<low<<endl;
                high++;
            }
            return ans;
        };
        return solve(goal)-solve(goal+1);
    }
};
// @lc code=end

int main(){
    Solution s;
    vector<int> nums{1,0,1,0,1};
    cout<<s.numSubarraysWithSum(nums,2)<<endl;
    return 0;
}