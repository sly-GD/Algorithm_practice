class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n=nums.size();
        vector<int> res;
        for(int x:nums){
            x=abs(x)-1;
            if(nums[x]>0)nums[x]=-nums[x];
        }
        for(int i=0;i<n;i++){
            if(nums[i]>0)res.push_back(i+1);
        }
        return res;
    }
};
