class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
    // 按照空格分割
        string ans(s,0,spaces[0]); //先取第一段
        spaces.push_back(s.length()); //末尾添加s的长度，处理最后一段
        for(int i=1;i<spaces.size();i++){
            ans+=' ';
            ans.append(s,spaces[i-1],spaces[i]-spaces[i-1]);
        }
    // 双指针
        // for(int i=0,j=0;i<s.size();i++){
        //     if(j<spaces.size() && spaces[j]==i){
        //         ans+=' ';
        //         j++;
        //     }
        //     ans+=s[i];
        // }
        return ans;
    }
};
