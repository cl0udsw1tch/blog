class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        M=len(tokens)
        if M==1:
            return int(tokens[0])
        
        stack=[]
        for m in range(M):
            token=tokens[m]
            if token=="+":
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
            elif token=="-":
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif token=="*":
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
            elif token=="/":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]