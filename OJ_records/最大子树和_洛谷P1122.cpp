#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

const int MAXN = 16010; // 题目约束：n ≤ 16000
vector<int> adj[MAXN];  // 邻接表（无向树）
int weight[MAXN];       // 节点权值
int dp[MAXN];           // dp[u]: 包含u的最大连通子图点权和
int ans = INT_MIN;      // 全局答案（初始化为最小整数）

// 树形DP：后序DFS
void dfs(int u, int parent) {
    dp[u] = weight[u]; // 至少包含自身
    for (int v : adj[u]) {
        if (v == parent) continue;
        dfs(v, u);
        if (dp[v] > 0) { // 贪心：仅合并正贡献子树
            dp[u] += dp[v];
        }
    }
    ans = max(ans, dp[u]); // 更新全局最优解
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    // 读入节点权值（1-indexed）
    for (int i = 1; i <= n; ++i) {
        cin >> weight[i];
    }
    
    // 建图（n-1条无向边）
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    // 任选根节点（1号）开始DFS
    dfs(1, 0);
    
    cout << ans << '\n';
    return 0;
}