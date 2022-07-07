#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        a = list(a)
        a.sort()
        b = list(b)
        b.sort()
        
        if len(a) != len(b):
            return False
            
        for i in range(len(a)):
            # print(a[i],b[i])
            if a[i] != b[i]:
                return False
                
        # print(a,b)
        return True
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends