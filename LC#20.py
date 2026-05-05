# 20. Valid Parentheses
class Solution:
    def validation(self, c):
        if(c=='('):
            return ')'
        elif (c=='['):
            return ']'
        elif (c=='{'):
            return '}'

    def isValid(self, s: str) -> bool:
        # print(s)
        length = len(s)
        stack = []
        if(length%2 == 1):
            return False
        else:
            for i in range(length):
                if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
                    stack.append(s[i])
                else:
                    if not stack:
                        return False
                    open = stack.pop()

                    if self.validation(open) != s[i]:
                        return False
            return not stack
                    
                    
                
        
