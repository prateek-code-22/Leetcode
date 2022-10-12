class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        
        n = len(nums)
        
        for i in range(n-2):
            a,b,c = nums[i:i+3]
        
            if (a + b > c) and (c + b > a) and (c + a > b):
                return a + b + c
        
        return 0