#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 100005; // 最大节点数，根据题目调整

// 邻接表存储图
vector<int> adj[MAXN];
// vector<list<int>> adj;  需要动态指定大小后访问 adj.resize(n);

int dfn[MAXN]; // 节点u的搜索次序（时间戳）
int low[MAXN]; // 节点u或u的子树能够追溯到的最早的栈中节点的次序号
bool is_cut[MAXN]; // 标记节点是否为割点
int timestamp; // 时间戳计数器

// Tarjan算法求割点
// u: 当前节点
// root: 当前搜索树的根节点
// parent: u的父节点
void tarjan(int u, int root, int parent) {
    int child_count = 0; // 记录根节点的子树数量
    dfn[u] = low[u] = ++timestamp; // 初始化dfn和low
    
    // 遍历所有邻接点
    for (int v : adj[u]) {
        if (dfn[v] == 0) { // 如果v未被访问过
            tarjan(v, root, u); // 递归访问v
            
            // 更新u的low值，取子节点v的low值较小者
            low[u] = min(low[u], low[v]);
            
            // 判断割点逻辑
            if (u != root && low[v] >= dfn[u]) {
                // 如果u不是根节点，且子节点v无法不经过u到达u的祖先，则u是割点
                is_cut[u] = true;
            }
            
            if (u == root) {
                // 如果u是根节点，累加子树数量
                child_count++;
            }
        } else if (v != parent) {
            // 如果v已被访问过，且v不是u的父节点（回边），更新u的low值
            low[u] = min(low[u], dfn[v]);
        }
    }
    
    // 如果u是根节点，且子树数量大于等于2，则u是割点
    if (u == root && child_count >= 2) {
        is_cut[u] = true;
    }
}

int main() {
    int n, m; // n个节点，m条边
    cin>>n>>m;
    
        // 初始化
        for (int i = 1; i <= n; i++) {
            adj[i].clear();
            dfn[i] = 0;
            low[i] = 0;
            is_cut[i] = false;
        }
        timestamp = 0;
        
        // 读入边
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        
        // 图可能不连通，需要遍历所有节点
        for (int i = 1; i <= n; i++) {
            if (dfn[i] == 0) {
                tarjan(i, i, 0); // i是当前连通块的根，父节点设为0
            }
        }
        vector<int> res;
        // 输出割点
        int cut_count = 0;
        for (int i = 1; i <= n; i++) {
            if (is_cut[i]) {
                res.push_back(i);
                cut_count++;
            }
        }
        sort(res.begin(), res.end());
        cout << cut_count << endl;
        for (auto v:res){
            cout << v << " ";
        }
    return 0;
}




// void tarjan(int u, int root, int parent){
//     int child_tree=0;
//     dfn[u]=low[u]=++timestamp;

//     for(int v:adj[u]){
//         if(dfn[v]==0){
//             tarjan(v,root,u);
//             low[u]=min(low[u],low[v]);

//             if (u!=root && low[v]>=dfn[u]){
//               is_cut[u]=true;
//             }
//             if(u==root){
//               child_tree++;
//             }  
//         }   
//         else if(v!=parent){
//             low[u]=min(low[u],low[v]);
//         }
//     }
//     if(u==root && child_tree>=2){
//         is_cut[u]=true;
//     }

// }