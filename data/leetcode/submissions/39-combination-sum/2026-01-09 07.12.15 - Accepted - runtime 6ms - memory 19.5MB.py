class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        M=len(candidates)

        def backtrack(total,i,curr):
            if total==target: return [curr[:]]

            r=[]
            for x in range(i,M):
                cand=candidates[x]
                if total+cand>target: continue
                curr.append(cand)
                r.extend(backtrack(total+cand,x,curr))
                curr.pop()
            return r
        return backtrack(0,0,[])