/*
 * @lc app=leetcode.cn id=1577 lang=cpp
 *
 * [1577] 数的平方等于两数乘积的方法数
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
    using ll= long long;
    inline int solve(vector<int>& a,vector<int>& b){
        int ans=0;
        for(int i=0;i<a.size();i++){
            int l=0,r=b.size()-1;
            while(l<=r){
                ll x=(ll)a[i]*a[i],y=(ll)b[l]*b[r];
                if(x==y){
                    if(b[l]==b[r]){
                        int count=r-l+1;
                        ans+=count*(count-1)/2;
                        break;
                    }else{
                        int count1=1,count2=1;
                        while(l+1<=r&&b[l+1]==b[l]){
                            l++;count1++;
                        }
                        while(r-1>=l&&b[r-1]==b[r]){
                            r--;count2++;
                        }
                        ans+=count1*count2;
                        l++;r--;
                    }
                }
                else if(x>y){
                    l++;
                }else{
                    r--;
                }
            }
        }
        return ans;
    }
public:
    int numTriplets(vector<int>& nums1, vector<int>& nums2) {
       const int n=nums1.size(),m=nums2.size();
       int ans=0;
       sort(nums1.begin(),nums1.end());
       sort(nums2.begin(),nums2.end());
        ans=solve(nums1,nums2)+solve(nums2,nums1);
       return ans;
    }
};
// @lc code=end

