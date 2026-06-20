class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # state i: numbers 1...i have been used 

        def backtrack(i,curr: set):
            if len(curr)==k:
                return [list(curr)]
            if k-len(curr)>n-i: return []

            r=[]
            for x in range(i+1,n+1):
                if x in curr: continue
                curr.add(x)
                r.extend(backtrack(x, curr))
                curr.remove(x)
            return r
        return backtrack(0, set())

