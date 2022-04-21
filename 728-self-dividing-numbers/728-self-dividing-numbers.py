class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(n):
            l = 0
            num = n
            c = 0 
            while num:    
                d = num % 10
                num = num // 10
                l +=1
                
                if d!=0 and n % d == 0:
                    c +=1
                    
            if c == l:
                return True
            return False
        
        res = []
        for i in range(left,right+1):
            if check(i):
                res.append(i)
        return res
        