class Solution:
    def numTrees(self, n: int) -> int:
        #catalan number 
        # 2n! / n! *(n+1)!
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)