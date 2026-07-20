class Solution {
public:
    bool canTransform(string start, string result) {
        string s=start,r=result;
        s.erase(remove(s.begin(),s.end(),'X'),s.end());
        r.erase(remove(r.begin(),r.end(),'X'),r.end());
        if(s!=r)return false;
        int n=start.size(),i=0,j=0;
        while(i<n && j<n){
            while(i<n && start[i]=='X'){
                i++;
            }
            while(j<n && result[j]=='X'){
                j++;
            }
            if((start[i]=='L' && j>i) || (start[i]=='R' && j<i)){
                return false;
            }
            i++;j++;
        } 
        return true;
    }
};
