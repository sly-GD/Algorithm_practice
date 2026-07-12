class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int n=grid.size(),m=grid[0].size();
        int i=0,j=m-1,res=0;
        while(i<n &&j>=0){
            if(grid[i][j]<0){
                res+=n-i;
                j--;
            }else{
                i++;
            }
        }
        //朴素遍历
        // for(;i>=0;i--){
        //     for(int j=m-1;j>=0;j--){
        //         if(grid[i][j]<0)res++;
        //         if(grid[i][j]>=0)break;
        //     }
        // }
        return res;
    }
};
