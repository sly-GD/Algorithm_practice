class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> yh[34];
        for(int i=0;i<34;i++){
            yh[i].resize(i+1,1); //利用resize（）初始化每行长度和初始值
            for(int j=1;j<i;j++){
                yh[i][j]=yh[i-1][j-1]+yh[i-1][j];
            }
        }
        return yh[rowIndex];
    }
};
