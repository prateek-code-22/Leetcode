class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        pre = []
        
        for i in range(rowIndex+1):
            row = []
            for j in range(0,i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pre[j-1] + pre[j])
                    
            pre = row
            res.append(row)
            
        return res[rowIndex]
            
            