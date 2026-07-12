class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]<=0)continue;
            if(nums[i]>n)continue;
            if(nums[i]!=nums[nums[i]-1])
                swap(nums[i],nums[nums[i--]-1]);  //交换后i不变，要重新验证新来的数字
        }
        for(int i=0;i<n;i++){
            if(nums[i]!=i+1)return i+1;
            if(i==n-1)return i+2;  // 如果数组内正整数全部有效，则返回n+1。
        }

        return 0;
    }
};
