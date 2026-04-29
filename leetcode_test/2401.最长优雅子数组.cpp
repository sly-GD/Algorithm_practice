/*
 * @lc app=leetcode.cn id=2401 lang=cpp
 *
 * [2401] 最长优雅子数组
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
//暴力枚举右端点
int longestNiceSubarray__(vector<int>& nums) {
        const int n=nums.size();
        int cnt=nums[0],res=1;
        for(int i=0;i<n;i++){
            int _or=0,j=i;
            while(j>=0&&(_or&nums[j])==0){
                _or|=nums[j];
                j--;
            }
            res=max(res,i-j);
        }
        return res;
    }
//滑动窗口
int longestNiceSubarray(vector<int>& nums) {
    const int n=nums.size();
    int res=1;
    for(int i=0,j=0,_or=0;i<n;i++){        
        while(_or & nums[i]){ //有交集
            _or^=nums[j++];
        }
        _or|=nums[i];
        res=max(res,i-j+1);
    }
    return res;
}
};
// @lc code=end

