class Solution {
public:
    //栈形式，占用额外空间
    bool backspaceCompare_0(string s, string t) {
        int n=s.size(),m=t.size();
        auto check=[](string x){
            vector<char> c;
            for(char p:x){
                if(p!='#')c.push_back(p);
                else{
                    if(!c.empty())
                    c.pop_back();
                }
            };
            return c;
        };
        vector<char> c1,c2;
        c1=check(s),c2=check(t);
        return c1==c2;
        
    }

    //双指针，无额外空间
    bool backspaceCompare(string s, string t) {
        int n=s.size(),m=t.size();
        int i=n-1,j=m-1;int skip1=0,skip2=0;
        while(i>=0 || j>=0){            
            while(i>=0){
                if(s[i]=='#'){
                    skip1++;i--;
                }else if(skip1>0){
                    skip1--;i--;
                }else{
                    break;//找到有效字符停止左移
                }
            }
            while(j>=0){
                if(t[j]=='#'){
                    skip2++;j--;
                }else if(skip2>0){
                    skip2--;j--;
                }else{
                    break;
                }
            }
            // 两种情况不匹配：
            // 1. 两边都有字符，但字符不等
            // 2. 一边有字符，一边已经走完
            if(i>=0 && j>=0){
                if(s[i]!=t[j])return false;
            }else if(i>=0 || j>=0){
                return false;
            }
            i--;j--; 
        }
       return true;
    }
    
};
