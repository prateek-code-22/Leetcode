class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(self,nums,target): 
            start =0 
            end = len(nums)-1
            res1 =-1
            
            while start<=end:
                mid = start+(end-start)//2
                if nums[mid]==target:
                    res1 =  mid
                    end = mid-1 
                elif target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            return res1
        
        def last(self,nums,target):
            
            start =0 
            end = len(nums)-1
            res2 =-1
            
            while start<=end:
                mid = start+(end-start)//2
                if nums[mid]==target:
                    res2 =  mid
                    start = mid+1 
                elif target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            return res2
        
        
            
        return first(self,nums,target),last(self,nums,target)
    
        
        
        
        