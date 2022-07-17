class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        hashMap = {}
        
        for i in range(n):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1

        for i in range(1,n+2):
            if i not in hashMap.keys():
                return i
                
        
        
            