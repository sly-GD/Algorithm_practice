// class Solution {
// public:
//     const int MOD=1e9+7;
//     int maxSum(vector<int>& nums1, vector<int>& nums2) {
//         int n=nums1.size(),m=nums2.size();
//         int i=0,j=0;
//         long long sum1=0,sum2=0;
//         long long res=0;
//         while(i<n && j<m){
//             if(nums1[i]==nums2[j]){
//                 res+=max(sum1,sum2)+nums2[j];
//                 ++i;++j;sum1=0;sum2=0;
//             }
//             else if(nums1[i]<nums2[j]){
//                 sum1+=nums1[i++];
//             }else{
//                 sum2+=nums2[j++];
//             }
//             //cout<<res<<endl;
//         }
//         for(;i<n;i++)sum1+=nums1[i];
//         for(;j<m;j++)sum2+=nums2[j];
//         return (res+max(sum1,sum2))%MOD;
//     }
// };

class Solution {
public:
    const int MOD = 1e9 + 7;
    int maxSum(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        int i = 0, j = 0;
        long long sum1 = 0, sum2 = 0, res = 0;
        
        while (i < n && j < m) {
            if (nums1[i] < nums2[j]) {
                sum1 += nums1[i++];
            } else if (nums1[i] > nums2[j]) {
                sum2 += nums2[j++];
            } else {
                res += (sum1 > sum2 ? sum1 : sum2) + nums2[j];
                ++i; ++j;
                sum1 = sum2 = 0;
            }
        }
        
        while (i < n) sum1 += nums1[i++];
        while (j < m) sum2 += nums2[j++];
        
        return (res + (sum1 > sum2 ? sum1 : sum2)) % MOD;
    }
};
