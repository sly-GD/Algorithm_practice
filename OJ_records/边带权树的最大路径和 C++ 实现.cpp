#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxPathSum(vector<vector<int>>& edges, int n) {
        // 构建邻接表：存储 {邻接点, 边权}
        vector<vector<pair<int, int>>> adj(n);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }

        long long maxSum = 0; // 使用 long long 防止溢出
        
        function<long long(int, int)> dfs = [&](int u, int parent) -> long long {
            long long first = 0, second = 0; // 最大和次大子树贡献
            
            for (auto& [v, w] : adj[u]) {
                if (v == parent) continue;
                
                long long childDown = dfs(v, u);
                long long value = w + childDown;
                
                if (value > first) {
                    second = first;
                    first = value;
                } else if (value > second) {
                    second = value;
                }
            }
            
            // 更新全局最大路径和（以 u 为最高点的路径）
            maxSum = max(maxSum, first + second);
            
            return first; // 返回从 u 向下的最大路径和
        };
        
        dfs(0, -1); // 从节点 0 开始 DFS
        return static_cast<int>(maxSum);
    }
};

// 示例用法
#include <iostream>
int main() {
    Solution sol;
    
    // 测试用例 1: 简单树
    //     0
    //    / \
    //   5   -3
    //  / \   \
    // 2   -1  4
    vector<vector<int>> edges1 = {{0, 1, 5}, {0, 2, -3}, {1, 3, 2}, {1, 4, -1}, {2, 5, 4}};
    cout << "Test 1: " << sol.maxPathSum(edges1, 6) << endl; // 预期输出: 7 (路径 3->1->0->2->5 或类似)
    
    // 测试用例 2: 全负边权
    vector<vector<int>> edges2 = {{0, 1, -2}, {1, 2, -3}};
    cout << "Test 2: " << sol.maxPathSum(edges2, 3) << endl; // 预期输出: 0 (单顶点路径最优)
    
    // 测试用例 3: 单节点
    vector<vector<int>> edges3 = {};
    cout << "Test 3: " << sol.maxPathSum(edges3, 1) << endl; // 预期输出: 0
    
    return 0;
}
