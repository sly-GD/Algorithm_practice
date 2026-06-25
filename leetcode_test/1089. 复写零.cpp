class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n=arr.size(),zerocnt=0;
        for(int x:arr){
            if(!x){
                zerocnt++;
            }
        }
        int tail=n-1+zerocnt;
        for(int i=n-1;i>=0;i--){
            if(tail<n){
                arr[tail]=arr[i];
            }
            tail--;
            if(!arr[i]){
                if(tail<n){
                    arr[tail]=0;
                }
                tail--;
            }
        }
    }
    void duplicateZeros_0(vector<int>& arr) {
        int n=arr.size();
        for(int i=0;i<n;i++){
            if(!arr[i]){
                for(int j=n-1;j>i+1;j--){
                    arr[j]=arr[j-1];
                }
                if(i==n-1)break;
                arr[i+1]=0;
                i++;
            }
        }
    }
};
