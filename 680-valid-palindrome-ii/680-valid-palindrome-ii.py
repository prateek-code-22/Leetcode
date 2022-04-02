class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                
                start += 1
                end -= 1

            return True
        
        
        n = len(s)
        start = 0 
        end = n - 1 
        count = 0
        
        while start < end:
            if s[start] != s[end]:
                return check(start+1, end) or check(start, end -1)
            else:
                
                start += 1
                end -= 1
        return True