class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        diff = 10000
        for cur_ind in range (len (nums)-1):
            left, right = cur_ind + 1, len(nums)-1 
            while left < right :
                threesum = nums[cur_ind] + nums[left] + nums[right]
                if threesum == target :
                    return threesum
                if abs(threesum - target) < diff:
                    diff = abs(threesum - target)
                    ans = threesum
                if threesum < target :
                    left += 1
                elif threesum > target:
                    right -= 1
        return ans