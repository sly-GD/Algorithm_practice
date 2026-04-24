#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

void get_fibonacci(ll n){
    vector<ll> fibs={1,2};
    while(fibs.back()<n){
        fibs.push_back(fibs[fibs.size()-1]+fibs[fibs.size()-2]);
    }

    vector<ll> indices;
    ll temp_n=n;
    for(int i=fibs.size()-1;i>=0;--i){
        if(temp_n>=fibs[i]){
            temp_n-=fibs[i];
            indices.push_back(i+1); // 存储下标，F1=1, F2=2...
        }
    }
    reverse(indices.begin(),indices.end());

    int k=indices.size();

    ll dp0=1;
    ll dp1=(indices[0]-1)/2;
    for(int i=1;i<k;++i){
        ll prev_dp0=dp0;
        ll prev_dp1=dp1;

        int gap=indices[i]-indices[i-1];

        dp0=prev_dp0+prev_dp1;
        dp1=prev_dp0*((gap-1)/2)+prev_dp1*(gap/2);

    }
    cout<<dp0+dp1<<endl;


}

int main(){
    ll n=0;
    cin>>n;
    //scanf("%d",&n);
    get_fibonacci(n);
    return 0;
}

// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// typedef long long ll;

// /**
//  * 解题思路：
//  * 1. 预处理斐波那契数列，注意题目定义的起始为 1, 2, 3, 5...
//  * 2. 贪心求出 n 的齐肯多夫表示（唯一的一组不相邻斐波那契数之和）。
//  * 3. 使用动态规划统计所有可能的拆分方案。
//  */

// void solve() {
//     ll n;
//     if (!(cin >> n)) return;

//     // 1. 生成斐波那契数列
//     vector<ll> fibs;
//     fibs.push_back(1);
//     fibs.push_back(2);
//     while (fibs.back() < n) {
//         fibs.push_back(fibs[fibs.size() - 1] + fibs[fibs.size() - 2]);
//     }
//     for (ll f: fibs){
//         cout<<f<<" ";
//     }
//     cout<<endl;
//     // 2. 贪心得到齐肯多夫表示的下标集合 (1-based index)
//     vector<int> indices;
//     ll temp_n = n;
//     for (int i = fibs.size() - 1; i >= 0; --i) {
//         if (temp_n >= fibs[i]) {
//             temp_n -= fibs[i];
//             indices.push_back(i + 1); // 存储下标，F1=1, F2=2...
//         }
//     }
//     // 将下标转为升序排列：x1, x2, ..., xk
//     reverse(indices.begin(), indices.end());
//     for (int i: indices){
//         cout<<i<<" "<<fibs[i-1]<<endl;

//     }
//     // 3. 动态规划
//     // dp0: 当前项不拆分的方案数
//     // dp1: 当前项进行拆分的方案数
//     int k = indices.size();
//     ll dp0 = 1;
//     ll dp1 = (indices[0] - 1) / 2;

//     for (int i = 1; i < k; ++i) {
//         ll prev_dp0 = dp0;
//         ll prev_dp1 = dp1;
//         cout<<"prev_dp0:"<<prev_dp0<<" prev_dp1:"<<prev_dp1<<endl;
//         int gap = indices[i] - indices[i-1];
        
//         // 当前项不拆分：前面项拆不拆都可以
//         dp0 = prev_dp0 + prev_dp1;
        
//         // 当前项拆分：
//         // 如果前一项不拆，当前项拆分产生的间隙中有 (gap-1)/2 种放法
//         // 如果前一项拆了，当前项拆分产生的间隙中有 gap/2 种放法
//         dp1 = prev_dp0 * ((gap - 1) / 2) + prev_dp1 * (gap / 2);
//     }

//     // 输出总方案数
//     cout << dp0 + dp1 << endl;
// }

// int main() {
//     // 优化输入输出效率
//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);

//     solve();

//     return 0;
// }