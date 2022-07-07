#User function Template for python3

class Solution:
    def checkDoorStatus(self, N):
        # code here
        door = [0]*N
        
        for i in range(1,N+1):
            ans = math.sqrt(i)
            if ans == int(ans):
                door[i-1] = 1
                
        return door
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ptr = ob.checkDoorStatus(N)
        print(*ptr)
# } Driver Code Ends