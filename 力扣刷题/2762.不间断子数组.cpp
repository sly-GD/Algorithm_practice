/*
 * @lc app=leetcode.cn id=2762 lang=cpp
 *
 * [2762] 不间断子数组
 */
#include <vector>
#include <algorithm>
#include <iostream>
#include <deque>
#include <cmath>
using namespace std;
// @lc code=start
#pragma optimize("O3")
#pragma target("avx2")
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        const int n = nums.size();
        int high=0,low=0;
        long long res=0;
        deque<int> max_deque,min_deque;
        while(high<n){
            while(!max_deque.empty() && nums[high]>max_deque.back()){
                max_deque.pop_back();
            }
            max_deque.push_back(nums[high]);
            cout<<"dayin"<<endl;
            for (int num : max_deque) {
                cout << num << " ";
            }
            cout<<endl;
            while(!min_deque.empty() && nums[high]<min_deque.back()){
                min_deque.pop_back();
            }
            min_deque.push_back(nums[high]);
            for (int num : min_deque) {
    cout << num << " ";
}
            cout<<endl;
            while(abs(nums[high]-max_deque.front())>2 || abs(nums[high]-min_deque.front())>2){
                //cout<<"low="<<low<<" high="<<high<<endl;
                //cout<<"maxv="<<maxv<<" minv="<<minv<<endl;
                if(max_deque.front()==nums[low])max_deque.pop_front();
                if(min_deque.front()==nums[low])min_deque.pop_front();
                low++;                
            }
            res += high-low+1;

            high++;
            //cout<<"maxv="<<maxv<<" minv="<<minv<<"wai"<<endl;

        }
        return res;
    }
};
// @lc code=end

int main(){
    Solution s;
    vector<int> a{65,66,67,66,66,65,64,65,65,64};
    cout<<s.continuousSubarrays(a)<<endl;
    return 0;
}
