class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        
        if(n<=1) return 0;
        
        int jump = 0, curr = 0, maxjump = 0;
        for(int i=0;i<n;i++){
            if(curr < i){
                jump++;
                curr = maxjump;
            }
            maxjump = max(maxjump,nums[i] + i);
                
        }
        
        return jump;
    }
};