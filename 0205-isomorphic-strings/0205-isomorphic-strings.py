class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # equal no of characters in both string and combination of both
        
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))