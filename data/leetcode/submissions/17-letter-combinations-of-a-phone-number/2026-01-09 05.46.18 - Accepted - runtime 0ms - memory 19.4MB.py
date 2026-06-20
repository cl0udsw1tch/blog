class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        M=len(digits)
    
        if M==1: 
            c=int(digits)
            return [chr(ord('a')+((3*(c-2)+i) if c<8 else 19+3*(c-8)+i)) \
                    for i in range(3 if c not in [7,9] else 4)
            ]

        def backtrack(m, curr):
            if m==M: return [curr]

            c=int(digits[m])
            r=[]
            for i in range(3 if c not in [7,9] else 4):
                curr+=chr(ord('a')+((3*(c-2)+i) if c<8 else 19+3*(c-8)+i))
                r.extend(backtrack(m+1,curr))
                curr=curr[:-1]
            return r
        return backtrack(0, "")