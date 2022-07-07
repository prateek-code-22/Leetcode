class Solution:
    def ExtractNumber(self,S):
        maxi = -1
        for st in S.split():
            if st.isdigit() and '9' not in st: 
            	maxi = max(maxi, int(st))
        return maxi
        
        
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        ans=ob.ExtractNumber(S)
        print(ans)   
# } Driver Code Ends