class Solution {
public:
    int smallestDifference(vector<int>& a, vector<int>& b) {
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        long long res = LLONG_MAX;
        int i = 0, j = 0;
        int n = a.size(), m = b.size();
        while (i < n && j < m) {
            long long temp = 1LL * a[i] - b[j]; // 转换为longlong操作
            res = min(res, llabs(temp));
            if(!res)break;
            temp <= 0 ? i++ : j++;
        }
        return (int)res; //最后要换回来
}
};
