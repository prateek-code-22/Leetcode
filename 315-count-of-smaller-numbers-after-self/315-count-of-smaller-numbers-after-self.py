class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        aux = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n):
            indx = bisect_left(aux,nums[i])
            res.append(indx)
            aux.pop(indx)
            
        return res