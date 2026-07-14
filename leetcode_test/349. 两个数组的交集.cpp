class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> st(nums1.begin(),nums1.end());
        vector<int> res;
        for(int x:nums2){
            if(st.erase(x)){// 如果x在nums1中，就插入res
                res.push_back(x);
            }
        }
        return res;
    }
};
