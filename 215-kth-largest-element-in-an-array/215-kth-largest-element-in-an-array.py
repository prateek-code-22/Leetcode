class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        from heapq import heappop, heappush, heapify
        
        heap = []
        heapify(heap)
        
        
        for i in range(len(nums)):
            heappush(heap,nums[i]*-1)
            
        count = 0

        
        while heap:
            count +=1
            if count == k:
                return heappop(heap)*-1
            
            heappop(heap)
            heapify(heap)
            
        
        