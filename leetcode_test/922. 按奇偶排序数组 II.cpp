class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int n= nums.size();
        int l=0,r=1;
        while(l<n && r<n){
            if(l<n && !(nums[l]&1)){
                l+=2;
            }
            else if(r<n && nums[r]&1){
                r+=2;
            }
            else {swap(nums[l],nums[r]);
            l+=2;
            r+=2;
            }
        }
        return nums;
    }
};
