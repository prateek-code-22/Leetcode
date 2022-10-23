class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        n = len(nums)
        for i in  range(n):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] +=1
                
        for i,j in dic.items():
            if j == 2:
                dup = i
                res.append(i)
        
        apSum = (n*(n+1))//2 
        numSum = sum(nums)-dup
        miss = apSum - numSum
        res.append(miss)
        
        return res
        