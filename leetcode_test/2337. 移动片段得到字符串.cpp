class Solution {
public:
    bool canChange_0(string s, string t) {
        int n=s.size();
        //去除所以“_”后，字符串应该一样
        string start=s,target=t;
        start.erase(remove(start.begin(),start.end(),'_'),start.end());
        target.erase(remove(target.begin(),target.end(),'_'),target.end());
        if(start!=target)return false;

        for(int i=0,j=0;i<n;i++){
            if(s[i]=='_')continue;
            while(t[j]=='_')++j;

            if(s[i]=='L' && i<j || s[i]=='R'&& i>j) return false;
            ++j;
        }
        return true;

    }
    //无预处理版
        bool canChange(string s, string t) {
        int n = s.size();
        int i = 0, j = 0;
        while (i < n || j < n) {
            // 跳过s中的下划线
            while (i < n && s[i] == '_') i++;
            // 跳过t中的下划线
            while (j < n && t[j] == '_') j++;

            // 两者同时遍历结束，匹配成功
            if (i == n && j == n) return true;
            // 一个走完一个没走完，字符序列不一致
            if (i == n || j == n) return false;
            // 字符不相等，直接失败
            if (s[i] != t[j]) return false;

            // L只能左移：s中L的下标必须 >= t中L下标
            if (s[i] == 'L' && i < j) return false;
            // R只能右移：s中R的下标必须 <= t中R下标
            if (s[i] == 'R' && i > j) return false;

            i++, j++;
        }
        return true;
    }
};
