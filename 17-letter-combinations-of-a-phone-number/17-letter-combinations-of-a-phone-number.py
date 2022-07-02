class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mappingDigit = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"qprs","8":"tuv","9": "wxyz"}

        def backtrack(index,curr,mappingDigit):

            if len(digits)==len(curr):
                res.append(curr)
                return 

            #add each values of digit in current string
            for i in mappingDigit[digits[index]]:
                backtrack(index+1,curr+i,mappingDigit)

        #till digits is not null
        if digits:
            backtrack(0,"",mappingDigit)

        return res




        
        