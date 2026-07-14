class Solution {
public:
    //哈希表形式
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_map<int,int> cnt; //统计nums1中的数字出现次数
        for(int x:nums1){
            cnt[x]++;
        }
        for(int x:nums2){
            if(cnt[x]>0){
                cnt[x]--;
                res.push_back(x);
            }
        }
        return res;
    }

    //双指针写法
    vector<int> intersect_0(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        int i=0,j=0,n=nums1.size(),m=nums2.size();
        while(i<n && j<m){
            int x=nums1[i],y=nums2[j];
            if(x==y){
                res.push_back(x);
                i++;j++;continue;
            }
            if(x<y){
                i++;
            }else{
                j++;
            }
        }
        return res;
    }    
};
