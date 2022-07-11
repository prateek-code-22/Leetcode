class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        min_so_far = arr[0]
        maxProfit = 0
        n = len(arr)
        
        for i in range(0,n):
            min_so_far = min(min_so_far,arr[i])
            profit = abs(min_so_far-arr[i])
            maxProfit = max(profit,maxProfit)
        
        return maxProfit