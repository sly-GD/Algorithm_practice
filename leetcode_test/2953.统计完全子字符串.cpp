/*
 * @lc app=leetcode.cn id=2953 lang=cpp
 *
 * [2953] 统计完全子字符串
 */
#include <string>
#include <unordered_map>
#include <cmath>
#include <iostream>
#include <cassert>
#include <vector>
using namespace std;
// @lc code=start
class Solution {
private:
    int f(string s,int k){
        int res=0;
        for(int i=1;i<=26;i++){
            if(i*k>s.size())break;
            int window_size=i*k;
            
            int c[27]{};
            vector<int> x(window_size+1,0);
            for(int j=0;j<window_size;j++){
                c[s[j]-'a']++;
            }
            for(int j=0;j<26;j++){
                if(c[j]<=window_size)x[c[j]]++;
            }
            if(x[k]==i)res++;   
            for(int j=window_size,low=0;j<s.size();j++,low++){
                x[c[s[low]-'a']]--;
                c[s[low]-'a']--;
                x[c[s[low]-'a']]++;
                x[c[s[j]-'a']]--;
                c[s[j]-'a']++;
                x[c[s[j]-'a']]++;

                if(x[k]==i)res++;
            }
        }
        return res;
        
    }
public:
    int countCompleteSubstrings(string word, int k) {
        int n=word.size(),start=0,cnt=0;
        for(int i=1;i<=n;i++){
            if(i==n || abs((int)word[i]-(int)word[i-1])>2){
                cnt+=f(word.substr(start,i-start),k);
                start=i;
            }
        }
        return cnt;
    }
};
/*
二位前缀和优化去除了哈希表的冲突处理和访问时间
*/
// class Solution {
// public:
//     int countCompleteSubstrings(string word, int k) {
//         int n = word.size();
//         vector<vector<int>> prefix(26,vector<int>(n+1,0));
//         for(int i=0;i<n;i++){
//             int c = word[i]-'a';
//             for(int j=0;j<26;j++){
//                 prefix[j][i+1]=prefix[j][i];
//             }
//             prefix[c][i+1]++;
//         }
//         auto check = [&](int l,int r)->bool{
//             int count_chars=0;
//             for(int i=0;i<26;i++){
//                 int x=prefix[i][r+1]-prefix[i][l];
//                 if(x!=0 && x!=k)return false;
//                 if(x==k){
//                     count_chars++;
//                 }
//             }
//             return (r-l+1)==count_chars*k;
//         };
//         int cnt = 0,start=0;
//         for(int i=1;i<=n;i++){
//             if(i==n || abs(word[i]-word[i-1])>2){
//                 int end=i-1;
//                 int segLen=end-start+1; 
//                 for(int d=1;d<=26 && d*k<=segLen;d++){
//                     int windows_size=d*k;
//                     for(int l=start;l<=end-windows_size+1;l++){
//                         int r=l+windows_size-1;
//                         if(check(l,r)){
//                             cnt++;
//                         }
//                     }
//                 }
//                 start=i;   
//             }
//         }
//         return cnt;
//     }
// };


/*
该解答会超时
*/
// class Solution {
// private:
//     int countSegment(string segment,int k){
//         int cnt=0,len = segment.size();
//         for(int d=1;d<=26 && d*k<=len;d++){
//             int windows_size=d*k;
//             unordered_map<char,int> mp;
//             for(int i=0;i<windows_size;i++){
//                 mp[segment[i]]++;
//             }
//             //检查第一个窗口是否满足
//             if(is_valid_substring(mp,d,k)){
//                 cnt++;
//             }
//             for(int i=windows_size;i<len;i++){
//                 mp[segment[i]]++;
//                 mp[segment[i-windows_size]]--;
//                 if(mp[segment[i-windows_size]]==0){
//                     mp.erase(segment[i-windows_size]);
//                 }
//                 if(is_valid_substring(mp,d,k)){
//                     cnt++;
//                 }
//             }
//         }
//         return cnt;
//     }
//     bool is_valid_substring(unordered_map<char,int> mp,int d,int k){
//         if(mp.size()!=d){
//             return false;
//         }
//         for(auto [c,count]:mp){
//             if(count!=k){
//                 return false;
//             }
//         }
//         return true;
//     }
// public:
//     int countCompleteSubstrings(string word, int k){
//         int n = word.size(),cnt=0,start=0;
//         for(int i=1;i<=n;i++){
//             if(i==n || abs(word[i]-word[i-1])>2){
//                 cnt+=countSegment(word.substr(start,i-start),k);
//                 start=i;
//             }
//         }
//         return cnt;
//     }
    
// };
// @lc code=end
void testCountCompleteSubstrings() {
    Solution solution;
    
    // 测试用例1: 空字符串
    assert(solution.countCompleteSubstrings("", 1) == 0);
    
    // 测试用例2: 单个字符
    assert(solution.countCompleteSubstrings("a", 1) == 1);
    assert(solution.countCompleteSubstrings("a", 2) == 0);
    
    // 测试用例3: 所有字符相同
    assert(solution.countCompleteSubstrings("aaaa", 2) == 3);
    
    // 测试用例4: 连续字符且满足条件
    assert(solution.countCompleteSubstrings("abacaba", 1) == 7);
    assert(solution.countCompleteSubstrings("abacaba", 2) == 0);
    
    // 测试用例5: 混合情况
    assert(solution.countCompleteSubstrings("aabbcc", 2) == 3);
    assert(solution.countCompleteSubstrings("aabbcc", 1) == 6);
    
    // 测试用例6: 边界情况
    assert(solution.countCompleteSubstrings("aaabbb", 3) == 2);
    assert(solution.countCompleteSubstrings("aaabbb", 2) == 0);
    
    // 测试用例7: 长字符串
    assert(solution.countCompleteSubstrings("abcabcabc", 3) == 3);
    assert(solution.countCompleteSubstrings("abcabcabc", 1) == 9);
    
    // 测试用例8: 字符差值超过2
    assert(solution.countCompleteSubstrings("ad", 1) == 0);
    assert(solution.countCompleteSubstrings("ace", 1) == 0);
    
    // 测试用例9: 字母表边界
    assert(solution.countCompleteSubstrings("yzz", 1) == 3);
    assert(solution.countCompleteSubstrings("yzz", 2) == 0);
    
    // 测试用例10: 混合字母和数字
    assert(solution.countCompleteSubstrings("ab12", 1) == 0);
    
    cout << "所有测试用例通过!" << endl;
}

int main() {
    testCountCompleteSubstrings();
    return 0;
}
