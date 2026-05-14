/*
 * @lc app=leetcode.cn id=3862 lang=cpp
 *
 * [3862] 找出最小平衡下标
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2") 
class Solution {
public:
    //双指针解法
    int smallestBalancedIndex(vector<int>& nums) {
        using ll=long long;
        int n=nums.size();
        int l=0,r=n-1;
        ll sum=0,mul=1;
        while(l<r){
            if(sum<mul){
                sum+=nums[l++];
            }else{
                if(mul>(ll)1e14/nums[r])return -1;
                mul*=nums[r--];
            }
        }
        return sum==mul?l:-1;
    }
    
    
    //前缀和解法
        int smallestBalancedIndex_01(vector<int>& nums) {
        using ll=long long;
        int n=nums.size();
        ll sum=reduce(nums.begin(),nums.end()-1,0LL);
        if(n==1)return -1;
        vector<ll> pre(n+1,0);
        // for(int i=0;i<n;i++){
        //     pre[i+1]=pre[i]+nums[i];
        // }
        ll mul=1;
        for(int i=n-1;i>0;i--){
            if(sum==mul) return i;
            //pre单调减，mul单调增，如果pre[i]<mul，则pre[i]永远小于mul
            sum-=nums[i-1];
            if(mul>sum/nums[i])break;
            mul*=nums[i];
        }
        return -1;
    }
};
// @lc code=end

int main(){
    Solution s;
    vector<int> nums={1,1,4};
    cout<<s.smallestBalancedIndex(nums)<<endl;
    return 0;
}