class Solution:
    def simplifyPath(self, path: str) -> str:
        

        M=len(path)
        if M==1: return "/"
    
        stack=[]
        prev=""
        for m in range(1,M):
            c=path[m]
            if c!="/":
                prev+=c
                if m<M-1: continue

            if prev=="..":
                if stack: stack.pop()
            elif prev==".":
                pass
            elif prev:
                stack.append(prev)
            prev=""

        return "/"+"/".join(stack)
