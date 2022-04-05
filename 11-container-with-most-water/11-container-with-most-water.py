class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n-1
        res = 0
        
        while i<=j:
            
            area = min(nums[i],nums[j]) * (j-i)
            res = max(res,area)
            if nums[i]<nums[j]:
                i +=1
            else:
                j -=1
        return res
        