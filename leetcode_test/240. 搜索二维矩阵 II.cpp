class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n=matrix.size(),m=matrix[0].size();
        int i=0,j=m-1;
        while(i<n && j>=0){
            if(matrix[i][j]== target)return  true;

            if(matrix[i][j]<target){
                i++;
            }else{
                j--;
            }
        }
        // 朴素遍历
        // for(int i=n-1;i>=0;i--){
        //     if(matrix[i][0]>target)continue;
        //     for(int j=0;j<m;j++){
        //         if(matrix[i][j]==target)return true;
        //         if(matrix[i][j]>target)break;
        //     }
        // }
        return false;
    }
};
