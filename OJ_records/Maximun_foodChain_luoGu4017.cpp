#include <iostream>
#include <vector>
#include <list>
#include <queue>
using namespace std;

const int MOD=80112002;

template<typename T>
class Graph {
private:
    int V;  // 顶点数
    vector<list<T>> adj;  // 邻接表
    vector<int> inDegree;  // 入度数组
    vector<int> outDegree;  // 出度数组
    bool directed;  // 是否为有向图

public:
    // 构造函数
    Graph(int vertices, bool isDirected = false) 
        : V(vertices), directed(isDirected) {
        adj.resize(V);
        inDegree.resize(V, 0);
        outDegree.resize(V, 0);
    }

    // 添加边
    void addEdge(T u, T v) {
        adj[u].push_back(v);
        outDegree[u]++;
        inDegree[v]++;
        
        // 如果是无向图，需要添加反向边
        if (!directed) {
            adj[v].push_back(u);
            outDegree[v]++;
            inDegree[u]++;
        }
    }

    // 获取顶点数
    int getVertices() const {
        return V;
    }

    // 获取指定顶点的入度
    int getInDegree(T vertex) const {
        return inDegree[vertex];
    }

    // 获取指定顶点的出度
    int getOutDegree(T vertex) const {
        return outDegree[vertex];
    }

    // 获取指定顶点的邻接顶点列表
    const list<T>& getAdjacent(T vertex) const {
        return adj[vertex];
    }

    
    void decreaseInDegree(T vertex) {
        if (vertex >= 0 && vertex < V) {
            inDegree[vertex]--;
        }
    }


    // 打印所有顶点的入度和出度
    void printDegrees() const {
        cout << "顶点\t入度\t出度" << endl;
        for (int i = 0; i < V; i++) {
            cout << i << "\t" 
                 << inDegree[i] << "\t" 
                 << outDegree[i] << endl;
        }
    }

    // 打印邻接表
    void printAdjList() const {
        for (int i = 0; i < V; i++) {
            cout << i << " -> ";
            for (auto v : adj[i]) {
                cout << v << " ";
            }
            cout << endl;
        }
    }
};

// 使用示例
/*

int main() {
    // 创建一个有向图，包含5个顶点
    Graph<int> g(5, true);
    
    // 添加边
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    g.addEdge(4, 1);
    
    // 打印邻接表
    cout << "邻接表：" << endl;
    g.printAdjList();
    
    // 打印所有顶点的入度和出度
    cout << "\n顶点度数统计：" << endl;
    g.printDegrees();
    
    return 0;
}
*/
int main(){
    int n,m;
    cin>>n>>m;
    Graph<int> g(n+1,true);
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        g.addEdge(u,v);
    }
    //g.printAdjList();
    /*
用队列实现拓扑排序，按 “无依赖先计算” 的顺序处理节点：
先将所有入度为 0 的节点加入队列。
取出队首节点 u，遍历其所有后继节点 v：
转移：dp[v] = (dp[v] + dp[u]) % MOD（到 v 的路径数 = 原有路径数 + 从 u 延伸来的路径数）。
维护入度：in_degree[v]--，若 in_degree[v] == 0，将 v 加入队列。
    */
    vector<long long> dp(n+1,0);
    queue<int> q;
    long long res=0;
    for(int i=1;i<n+1;i++){
        if(g.getInDegree(i)==0){
            q.push(i);
            dp[i]=1;
        }
    }
    while(!q.empty()){
        int u=q.front();
        q.pop();
        for(auto v:g.getAdjacent(u)){
            dp[v]=(dp[v]+dp[u])%MOD;//转移：dp[v] = (dp[v] + dp[u]) % MOD（到 v 的路径数 = 原有路径数 + 从 u 延伸来的路径数）。
            g.decreaseInDegree(v);
            if(g.getInDegree(v)==0){
                q.push(v);
            }
        }
    }
    for (int i=1;i<n+1;i++){
        if(g.getOutDegree(i)==0){
            res=(res+dp[i])%MOD;
        }
    }
    cout<<res<<endl;
    return 0;
}