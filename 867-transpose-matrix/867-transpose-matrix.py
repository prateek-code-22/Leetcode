class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            newrow = []
            
            for j in range(len(matrix)):
                newrow.append(matrix[j][i])
                
            res.append(newrow)
            
        return res