class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = sum(nums)
        lsum = 0
        n = len(nums)
        
        for i in range(n):
            rsum -= nums[i]
            if lsum == rsum:
                return i
            else:
                lsum += nums[i]
                
                
        return -1