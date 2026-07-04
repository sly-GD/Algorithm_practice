class Solution {
public:
    //辅助数组
    bool isGood_0(vector<int>& nums) {
        int a[100]={0};
        int n=nums.size()-1;
        if(nums.size()==1)return false;
        for(int x:nums){
            if(x>n)return false;
            a[x]++;

        }
        for(int i=0;i<=n;i++){
            if(i==n && a[i]>2)return false;
            if(a[i]>1 && i<n)return false;
            //if(return false;
        }
        return true;
    }    
    //方法二：把 nums 当作辅助数组
    bool isGood(vector<int>& nums) {
        int n=nums.size()-1;
        int cnt_n=0;
        for(int x:nums){
            x=abs(x);
            if(x>n || (x==n && cnt_n>1) || (x<n && nums[x]<0)){
                return false;
            }
            if(x==n){
                cnt_n++;
            }
            else{
                nums[x]=-nums[x];
            }
        }
        return true;
    }
};
