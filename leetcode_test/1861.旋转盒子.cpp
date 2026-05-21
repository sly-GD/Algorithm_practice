/*
 * @lc app=leetcode.cn id=1861 lang=cpp
 *
 * [1861] 旋转盒子
 */
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        int m = boxGrid.size(), n = boxGrid[0].size();
        vector<vector<char>> x(n, vector<char>(m,'.'));
        //int z[m];memset(z,0,sizeof(z));
        for (int i = 0; i < m; ++i) {
            int bottom=n-1;
            for (int j = n - 1; j >= 0; --j) {
                if (boxGrid[i][j] == '*') {
                    x[j][m-i-1]='*';
                    bottom=j-1;
                }
                if(boxGrid[i][j]=='#'){
                    x[bottom][m-i-1]='#';
                    bottom--;
                }
            }
        }
        return x;
    }
};
// @lc code=end

