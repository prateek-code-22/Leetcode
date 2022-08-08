class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        col=[]
        for i in range(len(mat[0])):
            l=[]
            for j in mat:
                l.append(j[i])
            col.append(sum(l))

        row=[]
        for i in mat:
            row.append(sum(i))
            
            
        def check(mat,x,y):
            if row[x] == 1 and col[y] == 1:
                    return True
            return False


        n = len(mat)
        m = len(mat[0])
        count = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if check(mat,i,j):
                        count +=1
                        
        return count