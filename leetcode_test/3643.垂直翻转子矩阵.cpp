/*
 * @lc app=leetcode.cn id=3643 lang=cpp
 *
 * [3643] 垂直翻转子矩阵
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    vector<vector<int>> reverseSubmatrix(vector<vector<int>>& grid, int x, int y, int k) {
        int n = grid.size(), m = grid[0].size();
        for(int i=y;i<y+k;i++){
            for(int j=x;j<x+k/2;j++){
                swap(grid[j][i],grid[x+k-j-1+x][i]);
            }
        }
        return grid;
    }
};
// @lc code=end

