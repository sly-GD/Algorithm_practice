/*
 * @lc app=leetcode.cn id=2024 lang=cpp
 *
 * [2024] 考试的最大困扰度
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int n = answerKey.size();
        int left = 0, right = 0;
        int maxLen = 0;
        int maxT = 0;
        int maxF = 0;
        while (right < n) {
            if (answerKey[right] == 'T') {
                maxT++;
            }else {
                maxF++;
            }
            if (maxT <= k || maxF <= k) {
                maxLen = max(maxLen, right - left + 1);
            }else{
                if (answerKey[left] == 'T') {
                    maxT--;
                }else{
                    maxF--;
                }
                left++;
            }
            right++;
        }
        return maxLen;
    }
};
// @lc code=end

