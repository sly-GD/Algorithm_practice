/*
 * @lc app=leetcode.cn id=2875 lang=cpp
 *
 * [2875] 无限数组的最短子数组
 */
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    int minSizeSubarray(vector<int>& nums, int target) {
        const int n=nums.size();
        int l=0,r=0,res=INT_MAX;
        long long sum=0,temp=0;
        for(int x:nums)sum+=x;
        int rem=target%sum;
        if(rem==0)return (target/sum)*n;
        //cout<<"sum="<<sum<<" "<<"rem="<<rem<<endl;
        while(r<n*2){
            temp+=nums[r%n];
            while(temp>=rem){
                if(temp==rem){
                    res=min(res,r-l+1);
                }
                if(r-l+1>n)break;
                temp-=nums[l%n];
                l++;
            }
            r++;
        }
        return res==INT_MAX?-1:res+(target/sum)*n;
    }
};
// @lc code=end

int main(){
    Solution s;
    vector<int> nums={1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6};
    cout<<s.minSizeSubarray(nums,56)<<endl;
    return 0;
}