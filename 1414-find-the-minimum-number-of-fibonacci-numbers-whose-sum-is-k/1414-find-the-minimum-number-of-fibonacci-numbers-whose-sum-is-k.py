class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        res = [1,1]
        c = 0
        
        i = 2
        while True:
            if res[i-1] + res[i-2] > k:
                break
            res.append(res[i-1] + res[i-2])
            i +=1
            
        n = len(res)
        
        for i in range(n-1,-1,-1):
            if k>0 and k >= res[i]:
                k -= res[i]
                c += 1
            
        return c