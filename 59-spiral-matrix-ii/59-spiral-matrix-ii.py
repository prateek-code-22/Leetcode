class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [[0] * n for _ in range(n)]
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        dirx =0
        res = [[]*n]*n
        k=1
        
        while top<=bottom and left<=right:
            
            if dirx==0:
                for i in range(left,right+1):
                    # = i
                    mat[top][i] = k
                    k +=1
                top +=1   
            
            elif dirx==1:
                for i in range(top,bottom+1):
                    mat[i][right] = k
                    k +=1
                right -=1
                
            elif dirx==2:
                for i in range(right,left-1,-1):
                    mat[bottom][i] = k
                    k +=1
                bottom -=1
                
            elif dirx==3:
                for i in range(bottom,top-1,-1):
                    mat[i][left] = k
                    k +=1
                left +=1
                
            dirx = (dirx+1)%4
    
        for i in range(n):
            res[i] = (mat[i])
            
        return res