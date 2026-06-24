class Solution {
public:
    vector<int> transformArray(vector<int>& nums) {
        int i0=0;
        for(int i=0;i<nums.size();i++){
            if(!(nums[i]&1)){
                nums[i]=0;
                //cout<<"fds"<<endl;
            }else{
                nums[i]=1;
            }
        }
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                swap(nums[i],nums[i0++]);
            }
        }
        return nums;
    }
};
