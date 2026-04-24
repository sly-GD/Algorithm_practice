#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

class Solution{
    public:
    long long maximumLine(vector<int>& heights,int n,int k){
        // dp[mask][i]mask表示已选学生的集合，i表示最后一个学生是i
        // dp[mask][i]表示mask集合中最后一个学生是i的方案数
        // N<=16 所有学生集合有2^16种
        vector<vector<long long>> dp(1<<n,vector<long long>(n,0));
        for(int i=0;i<n;i++){ //initialize
            dp[1<<i][i] = 1;
        }
        for(int mask=0;mask < (1<<n);mask++){
            for(int i=0;i<n;i++){
                if(!(mask & (1<<i)))continue;
                if(dp[mask][i]==0)continue;
                for(int j=0;j<n;j++){
                    if(mask &(1<<j))continue;
                    if(abs(heights[i]-heights[j])>k){
                        int new_mask = mask | (1<<j);
                        dp[new_mask][j] += dp[mask][i];
                    }
                }
            }
        }
        long long ans =0;
        int full_mask = (1<<n) -1;
        for(int i=0;i<n;i++){
            ans += dp[full_mask][i]; //汇总所有方案数，最后一个同学可以是所有i
        }
        return ans;
    }
};

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,k;
    cin>>n>>k;
    vector<int> heights(n);
    for(int i=0;i<n;i++){
        cin>>heights[i];
    }

    Solution s;
    cout<<s.maximumLine(heights,n,k)<<endl;
    return 0;
}