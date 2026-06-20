class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        for c in s:
            if c=="(": stack.append(c)
            elif c==")":
                if not stack or stack.pop() != "(": return False
            elif c=="{":
                stack.append(c)
            elif c=="}":
                if not stack or stack.pop() != "{": return False
            elif c=="[":
                stack.append(c)
            elif c=="]":
                if not stack or stack.pop() != "[": return False
        
        return not stack