#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;
class Solution{
    public:
    int maximumRescuer(vector<int>& birds,vector<int>& food){
        int n=birds.size(),m=food.size();
        sort(birds.begin(),birds.end());
        sort(food.begin(),food.end());
        int i=0,j=0;
        int ans=0;
        while(i<n && j<m){
            if(birds[i]<=food[j]){
                ans++;
                i++;
            }
            j++;
        }
        return ans;
    }   
};

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin>>n>>m;
    vector<int> birds,food;
    birds.reserve(n);
    food.reserve(m);

    for(int i=0;i<n;i++){

        int x;
        cin>>x;
        birds.push_back(x);
    }
    for(int i=0;i<m;i++){
        int x;
        cin>>x;
        food.push_back(x);
    }
    Solution s;
    cout<<s.maximumRescuer(birds,food)<<endl;
    return 0;
}