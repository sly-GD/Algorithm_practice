/*
 * @lc app=leetcode.cn id=923 lang=cpp
 *
 * [923] 三数之和的多种可能
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        int MOD=1e9+7;
        int n=arr.size();
        sort(arr.begin(),arr.end());
        long long ans=0;
        for(int i=0;i<n-2;i++){
            int l=i+1,r=n-1;
            while(l<r){
                if(arr[i]+arr[l]+arr[r]==target){
                    int cntR=1,cntL=1;
                    while(l<r&&arr[l]==arr[l+1]){
                        cntL++;
                        l++;
                    }
                    while(l<r&&arr[r]==arr[r-1]){
                        cntR++;
                        r--;
                    }
                    if(arr[l]==arr[r]){
                        ans+=(long long)cntL*(cntL-1)/2;
                    }else{
                        ans+=(long long)cntL*cntR;
                    }
                    ans%=MOD;
                    l++;r--;
                
                }else{
                    if(arr[i]+arr[l]+arr[r]>target){
                        r--;
                    }else{
                        l++;
                    }
                }
            }
        }
        return (int)ans%MOD;
    }
};
// @lc code=end
int main(){
    Solution s;
    vector<int> arr={1,1,2,2,3,3,4,4,5,5};
    cout<<s.threeSumMulti(arr,8)<<endl;
    return 0;
}