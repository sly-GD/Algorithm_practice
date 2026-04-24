/*
 * @lc app=leetcode.cn id=2555 lang=cpp
 *
 * [2555] 两个线段获得的最多奖品
 */
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>
using namespace std;
// @lc code=start
class Solution {
public:
    //第二种写法
    int maximizeWin(vector<int>& prizePositions, int k) {
        int n = prizePositions.size();
        if(k*2+1>=prizePositions[n-1]+prizePositions[0]){
            return n;
        }
        
        int ans=0,left=0,right=0,mx=0;
        for(int mid=0;mid<n;mid++){
            while(right<n && prizePositions[right]-prizePositions[mid]<=k){
                right++;
            }   
            ans=max(ans,mx+right-mid);    
            while(prizePositions[mid]-prizePositions[left]>k){
                left++;
            }
            
            mx=max(mx,mid-left+1);
        }
        return ans;
    }
    //第一种写法
    int maximizeWin01(vector<int>& prizePositions, int k) {
        int n = prizePositions.size();
        if(k*2+1>=prizePositions[n-1]+prizePositions[0]){
            return n;
        }
        vector<int> mx(n+1);
        int ans=0,left=0;
        for(int right=0;right<n;right++){
            while(prizePositions[right]-prizePositions[left]>k){
                left++;
            }
            ans=max(ans,mx[left]+right-left+1);
            mx[right+1]=max(mx[right],right-left+1);
        }
        return ans;
    }
};
// @lc code=end

