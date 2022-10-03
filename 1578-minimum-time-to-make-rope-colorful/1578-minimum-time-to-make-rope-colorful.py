class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        prev = 0
        
        for i in range(1, len(s)):
            if s[i] == s[prev]:
                if cost[prev] < cost[i]:
                    ans += cost[prev]
                    prev = i
                else:
                    ans += cost[i]
            else:
                prev = i
                
        return ans 