class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        res = s.count(letter)
        return (res*100) // len(s)
        
        