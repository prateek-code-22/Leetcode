class Solution:
    def judgeCircle(self, s: str) -> bool:
        org1 = 0
        org2 = 0
        
        for drx in s:
            if drx == 'U':
                org1 += 1
            
            elif drx == 'D':
                org1 -= 1
            
            elif drx == 'R':
                org2 += 1
            
            elif drx == 'L':
                org2 -= 1
                    
        if org1 == 0 and org2 == 0:
            return True
        
        return False
                
        