/*
 * @lc app=leetcode.cn id=658 lang=cpp
 *
 * [658] 找到 K 个最接近的元素
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        const int n=arr.size();
        if(n==k)return arr;
        int l=0,r=n-k;
        while(l<r){
            int mid=(l+r)/2;
            if(x-arr[mid]>arr[mid+k]-x)l=mid+1;
            else r=mid;
        }
        return vector<int>(arr.begin()+l,arr.begin()+l+k);
    }
};
// @lc code=end

