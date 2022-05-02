class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []
        
        for i in range(len(number)):
            if number[i] == digit:
                num = (number[:i]) + (number[i+1:])
                res.append(int(num))
        
        return str(max(res))
        

            