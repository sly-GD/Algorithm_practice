#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;

typedef struct edge{
    int u,v,w;

    bool operator<(const edge& other) const{
        return w < other.w;
    }
}e; 
class Solution{
public:        
    vector<int> p;
    int find(int x){
        if(x != p[x])p[x]=find(p[x]);
        return p[x];
    }
    int findMaximumEdge(vector<e>& edge,int m,int n){
        //int n = edge.size();
        //p.clear();
        p.reserve(n+1);
        int ans=0,cnt=0;
        sort(edge.begin(),edge.end());
        for(int i = 1; i < n+1; i++)p[i]=i;
        for(int i=0;i<m;i++){
            int u = edge[i].u;
            int v=edge[i].v;
            int w=edge[i].w;
            if(find(u) != find(v)){
                p[find(u)] = find(v); 
                ans=max(ans,w);
                cnt++;               
            }
        }
        if(cnt!=n-1)return -1;
        return ans;

    }
};


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m; cin>>n>>m;
    Solution sol;
    vector<e> edge(m);
    for(int i=0;i<m;i++){
        int u,v,w; cin>>u>>v>>w;
        edge[i].u=u;
        edge[i].v=v;
        edge[i].w=w;
    }
    cout<<sol.findMaximumEdge(edge,m,n)<<endl;
    return 0;
}