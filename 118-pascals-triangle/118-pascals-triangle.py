class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        pre = []
        
        
        for i in range(numRows):
            row = []
            for j in range(0,i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pre[j-1]+pre[j])
                    
            pre = row
            res.append(row)
            
        return res