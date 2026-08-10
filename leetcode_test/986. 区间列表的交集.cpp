class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        vector<vector<int>> res;
        int i=0,j=0;
        int n=firstList.size(),m=secondList.size();
        res.reserve(n+m);
        while(i<n && j<m){
            auto& a=firstList[i],b=secondList[j];
            int l=max(a[0],b[0]),r=min(b[1],a[1]);
            if(l<=r) res.push_back({l,r});
            // if(a[1]<sb[1])i++;
            // else j++;
            a[1]<b[1]?++i:++j;
        }
        return res;
    }
};
