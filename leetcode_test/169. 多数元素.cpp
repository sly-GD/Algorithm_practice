class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        //摩尔投票
        int count=0,can=0;
        for(auto& x:nums){
            if(count==0){
                can=x;
                //count++;
            }
            
            if(x==can){
                count++;
            }else{
                count--;
            }
            
        }
        return can;
    }
};
