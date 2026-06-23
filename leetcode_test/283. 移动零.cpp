#include <vector>
using namespace std;
class Solution {
public:
    void moveZeroes_0(vector<int>& nums) {
        int n=nums.size();
        int stacktop=0;
        for(auto x:nums){
            if(x){
                nums[stacktop++]=x;
            }
        }
        for(int i=stacktop;i<n;i++){
            nums[i]=0;
        }

    }
    void moveZeroes(vector<int>& nums) {
        int i0=0;
        for(int& x:nums){
            if(x){
                swap(x,nums[i0]);
                i0++;
            }
        }
    }
};