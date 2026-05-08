/*
 * @lc app=leetcode.cn id=832 lang=cpp
 *
 * [832] 翻转图像
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        const int n=image.size(),m=image[0].size();
        for (int i=0;i<n;++i) {
            for(int j=0,k=n-1;j<=k;j++,k--){
                int a=image[i][j]^1,b=image[i][k]^1;
                image[i][j]=b;
                image[i][k]=a;
            }
        }
        // for (auto &row : image) {
        //     reverse(row.begin(), row.end());
        // }
        // for (auto &row : image) {
        //     for (auto &num : row) {
        //         num ^= 1;
        //     }
        // }
        return image;
    }
};
// @lc code=end

