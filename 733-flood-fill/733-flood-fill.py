class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        row = len(image)
        col = len(image[0])
        pixel = image[sr][sc]
        
        if pixel == color:
            return image
        
        def dfs(r,c):
            if image[r][c] == pixel:
                image[r][c] = color
                
                if r>=1:
                    dfs(r-1,c)
                if r+1 < row:
                    dfs(r+1,c)
                if c>=1:
                    dfs(r,c-1)
                if c+1 < col:
                    dfs(r,c+1)
                    
                    
        dfs(sr,sc)
        return image
    
                
        