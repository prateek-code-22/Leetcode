class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n= len(nums)
        i = 0
        j = n-1
        c = 0
        while i < j:
            sumz = nums[i] + nums[j]
            if sumz == k:
                c+=1
                i +=1
                j -=1
            elif sumz > k:
                j -=1
            else:
                i+=1
                
        return c
        