class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        start = 0
        end = n - 1
        
        while start<=end:
            mid = start + (end-start)//2
            
            if arr[mid] - (mid + 1) >= k:
                end = mid - 1
                
            else:
                start = mid + 1
                
        return end + k + 1
            
            