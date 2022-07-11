class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1
        
        #check for col1 if ele is 0
        for i in range(n):
            if matrix[i][0] == 0:
                col0 = 0 
                
            #check for matrix ele is 0 then mark in dummy
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(n-1,-1,-1):
            for j in range(m-1,0,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                            
            if col0 == 0:
                matrix[i][0] = 0
                
                