class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        '''
        f*(s) solves the subproblem assuming numbers have been chosen from
        mask=s[0], the current number is total=s[1]
        s: (mask, total) 
        x: 1...maxNumber to choose
            => s' = (mask | s, total + x)
        f(s, x) = not f*(s')
        f*(s) = any_x {f(s,x)}

        '''
        if desiredTotal <= 0:
            return True
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False

        memo={}
        def dfs(s):
            if s in memo:
                return
            (mask, total) = s
            for x in range(1, maxChoosableInteger + 1):
                bit = 1 << (x - 1)
                if mask & bit:
                    continue
                s_p=(mask | bit, total + x)
                dfs(s_p)
                if total + x >= desiredTotal or not memo[s_p]:
                    memo[s]=True
                    return
            memo[s]=False

        dfs((0, 0))
        return memo[(0,0)]