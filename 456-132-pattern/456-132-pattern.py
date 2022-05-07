class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        minValue = float('-inf')
        
        for i in nums[::-1]:
            if  i < minValue:
                return True
            
            while len(stack)!=0 and stack[-1]<i:
                minValue = stack.pop()
                
            stack.append(i)
            
        return False