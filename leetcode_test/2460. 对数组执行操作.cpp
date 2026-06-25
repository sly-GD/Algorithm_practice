class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n=nums.size();
        //vector<int> a;
        for(int i=0;i<n-1;){
            if(nums[i]==nums[i+1]){
                nums[i]*=2;
                nums[i+1]=0;
                i+=2;
                //a.push_back(i+1);
            }else i++;
        }
        // for(int x:a){
        //     nums[x]=0;
        // }
        for(int i0=0,i=0;i<n;i++){
            if(nums[i]){
                swap(nums[i],nums[i0]);
                i0++;
            }
        }
        return nums;
    }
};
