class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n==1: return ["()"]

        def backtrack(i,j,curr):
            if i+j==2*n: return [curr]

            r=[]
            if i<n:
                r.extend(backtrack(i+1, j, curr+"("))
            if j<n and i>j:
                r.extend(backtrack(i, j+1, curr+")"))
            return r
        return backtrack(0,0,"")
                
