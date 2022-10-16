class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        @cache
        def dp(i, left):
            if left == 1:
                return max(jobs[i:])
            maxDifficulty = 0
            ans = float('inf')
            for j in range(i, N - left + 1):
                maxDifficulty = max(maxDifficulty, jobs[j])
                ans = min(ans, maxDifficulty + dp(j + 1, left - 1))
            return ans
        
        N = len(jobs)
        if N < d:
            return -1
        return dp(0, d)
        