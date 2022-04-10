class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        n = len(ops)
        for i in range(n):
            
            if ops[i] == 'C':
                stack.pop()
            
            elif ops[i] == 'D':
                stack.append(stack[-1]*2)
                    
            elif ops[i] == '+':
                stack.append(stack[-1] + stack[-2])
            
            else:
                stack.append(int(ops[i]))
                
        return sum(stack)
        
            
        