class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {int n=houses.size(),m=heaters.size();
    sort(houses.begin(),houses.end());
    sort(heaters.begin(),heaters.end());
    int i=0,j=0,res=0;
    // while(i<n){
    //     while(j+1<m && abs(heaters[j+1]-houses[i])<=abs(heaters[j]-houses[i]))j++;
    //     res=max(res,abs(heaters[j]-houses[i]));
    //     i++;
    // }

    // 思路二：对每一个房子，二分查找离它最近的加热器（左边、右边各一个候选）
    for(int house:houses){
        auto it = lower_bound(heaters.begin(),heaters.end(),house); //二分查找第一个>=house的值
        int curmin = INT_MAX;
        if(it != heaters.end()){
            curmin=min(curmin,*it - house);
        }
        if(it != heaters.begin()){
            --it; //取左侧
            curmin=min(curmin,house-*it);
        }
        res=max(res,curmin);
    }
    return res;
    
    }
};
