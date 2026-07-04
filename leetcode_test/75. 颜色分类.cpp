class Solution {
public:
//两遍双指针
    void sortColors_0(vector<int>& nums) {
        int n = nums.size();
        int i0=0,i1=0;
        for(int i=0;i<n;i++){
            if(!nums[i]){
                swap(nums[i],nums[i0++]);
            }
        }
        for(int i=i0;i<n;i++){
            if(nums[i]==1){
                swap(nums[i],nums[i0++]);
            }
        }
    }
//插入排序
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int i0=0,i1=0;
        for(int i=0;i<n;i++){
            int x=nums[i];
            nums[i]=2;
            if(x<=1){
                nums[i0++]=1;
            }
            if(x==0){
                nums[i1++]=0;
            }
        }

    }
};
