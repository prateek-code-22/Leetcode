class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        
        if(n==0)
            return 0;
        
        
        int reach = 0;     
        
        for(int i=0;i<n;i++){
            if(reach<i){
                return false;
            }
            else{
                reach = max(reach, nums[i]+i);
            }
        }
        return true;
    }
};