# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorderele = []
        
        def solve(arr,k):
            n = len(arr)
            i,j = 0, n-1
            
            while (i<j):
                if (arr[i] + arr[j]) == k:
                    return True
                elif (arr[i] + arr[j]) < k:
                    i +=1
                elif (arr[i] + arr[j]) > k:
                    j -=1
                    
            return False
        
        def inorder(self,root):
            if root == None:
                return
            inorder(self,root.left)
            inorderele.append(root.val)
            inorder(self,root.right)
            
        inorder(self,root)
        return solve(inorderele,k)
        
        
    
        
        