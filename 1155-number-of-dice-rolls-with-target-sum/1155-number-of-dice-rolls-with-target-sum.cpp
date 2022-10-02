class Solution {
public:
    
    long long solve(int dice,int faces,int target){
        
        if(target < 0)
            return 0;
        if(dice == 0 && target != 0)
            return 0;
        if(target == 0 && dice != 0)
            return 0;
        if(dice == 0 && target == 0)
            return 1;
        
        long long ans = 0;
        for(int i = 1; i<=faces; i++){
            ans += solve(dice-1, faces, target-i);
        }
        return ans;
    }
    
    long long solveTd(int dice,int faces,int target,vector<vector<long long>> &dp){
        
        if(target < 0)
            return 0;
        if(dice == 0 && target != 0)
            return 0;
        if(target == 0 && dice != 0)
            return 0;
        if(dice == 0 && target == 0)
            return 1;
        
        if(dp[dice][target] != -1)
            return dp[dice][target];
        
        long long ans = 0;
        for(int i = 1; i<=faces; i++){
            ans = (ans + solveTd(dice-1, faces, target-i,dp))% 1000000007;
        }
        return dp[dice][target] = ans;
        
    }
    
    
    int numRollsToTarget(int n, int k, int target) {
        // return solve(n,k,target);
        vector<vector<long long>>dp(n+1,vector<long long>(target+1,-1));
        return solveTd(n,k,target,dp);
    
    }
};