class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
                
            elif nums[mid] > nums[mid-1]:
                start = mid + 1
                
            else:
                end = mid
                
        return start
                    
        