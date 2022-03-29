class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        while i<n-1:
            if nums[i] == nums[i+1]:
                return nums[i]
            
            i +=1
            
    
        