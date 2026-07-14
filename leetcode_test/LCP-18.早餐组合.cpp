constexpr long long MOD=1e9+7;
class Solution {
public:
  //二分查找
int breakfastNumber(vector<int>& staple, vector<int>& drinks, int x) {        
        int ans=0;
        sort(staple.begin(),staple.end());
        sort(drinks.begin(),drinks.end());
        int m=drinks.size();
        for(int s:staple){
            if(s>x)break;
            int limit=x-s;
            int cnt=upper_bound(drinks.begin(),drinks.end(),limit)-drinks.begin(); //二分查找
            ans+=cnt;
            if(ans>=MOD)ans-=MOD;
        }
        return static_cast<int>(ans%MOD);
    }    
    //双指针
    int breakfastNumber_1(vector<int>& staple, vector<int>& drinks, int x) {       
        int ans=0;
        sort(staple.begin(),staple.end());
        sort(drinks.begin(),drinks.end(),[](int a,int b){
            return a>b;
        });
        int i=0,j=0,n=staple.size(),m=drinks.size();
        while(i<n && j<m){
            if(staple[i]>x)break;
            if(staple[i]+drinks[j]<=x){
                ans+=m-j;
                ans%=MOD;
                i++;
            }else{
                j++;
            }
        }

        return ans;
    }
    
    //前缀和方法
    int breakfastNumber_0(vector<int>& staple, vector<int>& drinks, int x) {
        
        int ans=0;
        vector<int> cnt(x+1,0);
        for(int s:staple){
            if(s<=x)cnt[s]++;
        }
        for(int i=1;i<=x;i++){
            cnt[i]+=cnt[i-1];
            if(cnt[i]>=MOD)cnt[i]%=MOD;
        }

        for(int d:drinks){
            if(d<=x){
                ans+=cnt[x-d];
                ans%=MOD;
            }
        }
        return ans;
    }
};
