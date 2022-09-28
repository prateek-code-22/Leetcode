class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1);
        for(int i =0; i<=n; i++){
            ans[i] = countOnes(i);
        }
        return ans;
    }
private:
        int countOnes(int k){
            int one = 0;
            while(k > 0){
                if(k&1) one++;
                k >>= 1;  // right sift
            }
            return one;
        }

};
