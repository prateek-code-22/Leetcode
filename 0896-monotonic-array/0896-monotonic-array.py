class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        def checkdec(nums):
            n = len(nums)
            for i in range(n-1):
                if nums[i] >= nums[i+1]:
                    continue
                else:
                    return False
                
            return True
        
        def checkInc(nums):
            n = len(nums)
            for i in range(n-1):
                if nums[i] <= nums[i+1]:
                    continue
                else:
                    return False
            return True
        
        if len(nums) == 1:
            return True
        n = len(nums)
        
        if nums[0] > nums[n-1]:
            return checkdec(nums)
        else:
            return checkInc(nums)
    
        