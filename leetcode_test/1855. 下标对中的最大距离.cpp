class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size(),m=nums2.size();
        int j=0,res=0,i=0;
        while(j<m){
            while(i<n&&nums1[i]>nums2[j]){
                i++;
            }
            if(i==n)break;
            res=max(res,j-i);
            j++;
        }
        return res;
    }
};
