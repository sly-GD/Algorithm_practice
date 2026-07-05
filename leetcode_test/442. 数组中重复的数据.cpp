class Solution {
public:
    //将负数形式进行哈希标记
    vector<int> findDuplicates(vector<int>& nums) {
        int n=nums.size();
        vector<int> res;
        for(int i=0;i<n;i++){
            int x=abs(nums[i])-1;
            if(nums[x]<0)res.push_back(x+1);
            else nums[x]=-nums[x];
        }
        return res;
    }
};
