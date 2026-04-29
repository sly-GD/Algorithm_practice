/*
 * @lc app=leetcode.cn id=925 lang=cpp
 *
 * [925] 长按键入
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int n=name.size(),m=typed.size();
        for(int i=0,j=0;i<n||j<m;){
            if(i<n&&j<m&&name[i]==typed[j]){
                i++;
                j++;
            }
            else if(j>0&&typed[j]==typed[j-1])j++;
            else return false;
        }
        return true;
    }
};
// @lc code=end

