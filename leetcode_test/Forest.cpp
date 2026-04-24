#include <algorithm>
#include <vector>
#include <iostream>
#include <numeric>
#include <set>

using namespace std;

struct DSU {
    vector<int> parent;

    DSU(int n){
        parent.resize(n+1);
        iota(parent.begin(),parent.end(),0);
    }

    int find(int x){
        if(parent[x]==x){
            return x;
        }
        return parent[x]=find(parent[x]);
    }

    bool unite(int x,int y){
        int a=find(x);
        int b=find(y);
        if (a==b){
            return false;
        }
        parent[a]=b;
        return true;
    }

    bool connected(int x,int y){
        return find(x)==find(y);
    }
};

int main(){

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m1,m2;
    cin>>n>>m1>>m2;

    DSU dsuA(n),dsuB(n);

    for(int i=0;i<m1;i++){
        int a,b;
        cin>>a>>b;
        dsuA.unite(a,b);
    }
    
    
    for(int i=0;i<m2;i++){
        int a,b;
        cin>>a>>b;
        dsuB.unite(a,b);
    }

    vector<pair<int,int>> ans;
    //第一阶段，将所有与1不连通的点与1连通
    for(int i=2;i<=n;i++){
        bool a=!dsuA.connected(i,1)&&!dsuB.connected(i,1);
        if(a){
            dsuA.unite(i,1);
            dsuB.unite(i,1);
            ans.push_back({1,i});
        }
    }
        
    //第二阶段，处理“偏科”的点，只在一棵树中与1连接
    vector<int> L,R;
    set<int> seenA,seenB;
    for(int i=2;i<=n;i++){
        if(!dsuA.connected(i,1)){
            int root=dsuA.find(i);
            if(seenA.find(root)==seenA.end()){
                L.push_back(i);
                seenA.insert(root);
            }
        }
    }
    for(int i=2;i<=n;i++){
        if(!dsuB.connected(i,1)){
            int root=dsuB.find(i);
            if(seenB.find(root)==seenB.end()){
                R.push_back(i);
                seenB.insert(root);
            }
        }
    }
    int x=min(L.size(),R.size());
    for(int i=0;i<x;i++){
        ans.push_back({L[i],R[i]});
    }

    for(auto &p:ans){
        if(p.first>p.second){
            swap(p.first,p.second);
        }
    }

    sort(ans.begin(),ans.end());

    cout<<ans.size()<<endl;
    for(auto &p:ans){
        cout<<p.first<<" "<<p.second<<endl;
    }
    
    return 0;
}

//
//
// #include <algorithm>
// #include <vector>
// #include <iostream>
// #include <numeric>

// using namespace std;

// // 并查集结构
// struct DSU {
//     vector<int> parent;
//     DSU(int n) {
//         parent.resize(n + 1);
//         iota(parent.begin(), parent.end(), 0);
//     }
//     int find(int x) {
//         if (parent[x] == x) return x;
//         return parent[x] = find(parent[x]); // 路径压缩
//     }
//     bool unite(int x, int y) {
//         int a = find(x);
//         int b = find(y);
//         if (a == b) return false;
//         parent[a] = b;
//         return true;
//     }
//     bool connected(int x, int y) {
//         return find(x) == find(y);
//     }
// };

// int main() {
//     // 提升 I/O 性能
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int n, m1, m2;
//     if (!(cin >> n >> m1 >> m2)) return 0;

//     DSU dsuA(n), dsuB(n);

//     for (int i = 0; i < m1; i++) {
//         int u, v; cin >> u >> v;
//         dsuA.unite(u, v);
//     }
//     for (int i = 0; i < m2; i++) {
//         int u, v; cin >> u >> v;
//         dsuB.unite(u, v);
//     }

//     vector<pair<int, int>> ans;

//     // 第一阶段：将能连到1的点全部连上
//     for (int i = 2; i <= n; i++) {
//         // 如果在两棵树中，i 都没跟 1 连通
//         if (!dsuA.connected(1, i) && !dsuB.connected(1, i)) {
//             dsuA.unite(1, i);
//             dsuB.unite(1, i);
//             ans.push_back({1, i}); // 修复点：必须在 if 里面
//         }
//     }

//     // 第二阶段：处理“偏科”的点
//     vector<int> L, R;
//     vector<bool> visA(n + 1, false), visB(n + 1, false);

//     for (int i = 2; i <= n; i++) {
//         // 在森林 A 中还没跟 1 连通的点
//         if (!dsuA.connected(1, i)) {
//             int root = dsuA.find(i);
//             if (!visA[root]) {
//                 visA[root] = true;
//                 L.push_back(i);
//             }
//         }
//         // 在森林 B 中还没跟 1 连通的点
//         if (!dsuB.connected(1, i)) {
//             int root = dsuB.find(i);
//             if (!visB[root]) {
//                 visB[root] = true;
//                 R.push_back(i);
//             }
//         }
//     }

//     // 两边配对：一个在A中没连1的点 + 一个在B中没连1的点
//     // 连接它们后，在A中它们会通过1连通，在B中同理，且不会产生环
//     size_t sz = min(L.size(), R.size());
//     for (size_t i = 0; i < sz; i++) {
//         ans.push_back({L[i], R[i]});
//     }

//     // 格式化输出：先确保每对边 (u, v) 满足 u < v，再进行整体排序
//     for (auto &p : ans) {
//         if (p.first > p.second) swap(p.first, p.second);
//     }
//     sort(ans.begin(), ans.end());

//     cout << ans.size() << "\n";
//     for (auto &p : ans) {
//         cout << p.first << " " << p.second << "\n";
//     }

//     return 0;
// }