/*
 * @lc app=leetcode.cn id=2271 lang=cpp
 *
 * [2271] 毯子覆盖的最多白色砖块数
 */
#include <bits/stdc++.h> 
using namespace std;
class Solution {
public:
    int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
        // 1. 按左端点排序（基础步骤）
        sort(tiles.begin(), tiles.end());
        int n = tiles.size();
        int left = 0;
        long long sum = 0;
        int ans = 0;

        for (int right = 0; right < n; ++right) {
            int l = tiles[right][0];
            int r = tiles[right][1];
            sum += r - l + 1;

            // 核心：地毯右端贴当前瓷砖末尾，计算地毯左边界
            // 当左指针瓷砖 完全在地毯左侧 → 移出窗口
            while (tiles[left][1] < r - carpetLen + 1) {
                sum -= tiles[left][1] - tiles[left][0] + 1;
                left++;
            }

            // 计算当前覆盖的瓷砖数：总长度 - 左瓷砖没被覆盖的部分
            int cover = sum - max(0, (r - carpetLen + 1) - tiles[left][0]);
            ans = max(ans, cover);
        }
        return ans;
    }
};
 // @lc code=end

