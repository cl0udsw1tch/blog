class Solution:
    def calculate(self, s: str) -> int:

        arr=[]
        M=len(s)
        for m in range(M):
            token=s[m]
            if token==" ": continue
            if token.isalnum() and arr and arr[-1].isalnum():
                arr[-1]+=token
            else:
                arr.append(token)
        M=len(arr)

        if M==1:
            return int(arr[0])

        stack=[]
        arr=arr[::-1]
        while arr:
            token=arr.pop()
            if token=="(":
                stack.append(token)
            elif token==")":
                a=stack.pop()
                arr.append(a)
                stack.pop()
            elif token=="+":
                stack.append(token)
            elif token=="-":
                stack.append(token)
            else:
                if stack and stack[-1] in ["+","-"]:
                    if stack[-1]=="+":
                        stack.pop()
                        a=stack.pop()
                        arr.append(a+int(token))
                    else:
                        stack.pop()
                        if not stack or not isinstance(stack[-1], int):
                            arr.append(-int(token))
                        else:
                            a=stack.pop()
                            arr.append(a-int(token))
                else:
                    stack.append(int(token))

        return stack[0]