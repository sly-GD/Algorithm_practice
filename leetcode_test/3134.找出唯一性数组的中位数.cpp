/*
 * @lc app=leetcode.cn id=3134 lang=cpp
 *
 * [3134] 找出唯一性数组的中位数
 */
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <unordered_map>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
constexpr int MX=1e5+1;
int cnt[MX];
bitset<MX> st;
class Solution {
public:
    int medianOfUniquenessArray(vector<int>& nums) {
        const int n= nums.size();
        //int upper=0;
        st.reset();
        for(auto x:nums)st.set(x);
        using ll = long long;
        int right=st.count(),left=0;
        ll need=((ll)n*(n+1)/2+1)/2;
        auto check = [&](int upper)->bool{
            ll s=0;
            int k=0;
            memset(cnt,0,sizeof(cnt));
            int high=0,low=0;
            while(high<n){
                k+=(++cnt[nums[high]]==1);
                while(k>upper){
                    k-=(--cnt[nums[low]]==0);
                    low++;
                }
                s+=high-low+1;
                high++;
            }
            return s>=need;
        };

        while(left+1<right){
            int mid=(left+right)>>1;
            (check(mid)?right:left)=mid;
        }
        return right;

    }
};
// @lc code=end

