class Solution {
public:
    //排序+双指针
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        int n=arr1.size(),m=arr2.size();
        sort(arr2.begin(),arr2.end());
        sort(arr1.begin(),arr1.end());
        int res=0;
        int j=0;
        for(int x:arr1){
            while(j<m && arr2[j]<x-d){
                j++;  // 用j维护最小满足arr2[j]<x-d的下标
            }
            if(j==m || arr2[j]>x+d){
                res++;
            }
        }

        return res;
    }
    // 排序+二分查找
    int findTheDistanceValue_0(vector<int>& arr1, vector<int>& arr2, int d) {
        int n=arr1.size(),m=arr2.size();
        sort(arr2.begin(),arr2.end());
        int res=0;
        for(int i=0;i<n;i++){
            auto it = ranges::lower_bound(arr2,arr1[i]-d);  // 目的是要确定没有元素落在[x-d,x+d],
            // lower_bound() 返回一个迭代器，起始于arr2中第一个大于x-d的元素
            if(it==arr2.end() || *it>arr1[i]+d){
                res++;
            }
        } 
        return res;
    }
};
