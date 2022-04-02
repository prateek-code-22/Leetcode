class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0 
        end = num
        
        while start<=end:
            mid = start+(end-start)//2
            sq = mid**2

            if sq == num:
                return True
            
            elif sq > num:
                end = mid - 1
            
            else:
                start = mid + 1
        
        return False
        