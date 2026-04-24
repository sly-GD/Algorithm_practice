/*
 * @lc app=leetcode.cn id=2799 lang=cpp
 *
 * [2799] 统计完全子数组的数目
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        const int n = nums.size();
        int res=0;
        int high=0,low=0,cnt=0;
        int x[2001]={0};
        for(int i:nums){
            if(x[i]==0){
                cnt++;
            }
            x[i]++;
        }
        int y[2001]={0},temp=0;
        //cout<<cnt<<endl;
        while(high<n){
            if(y[nums[high]]==0){
                temp++;
            }
            y[nums[high]]++;
            while(temp==cnt){
                res+=n-high;
                //cout<<"res="<<res<<"temp="<<temp<<endl;
                y[nums[low]]--;
                if(y[nums[low]]==0){
                    temp--;
                }
                low++;
            }
            high++;
        }
        return res;
    }
};

// @lc code=end

