class Solution:
    def minSteps(self, n: int) -> int:
        
        if n==1: return 0
        if n==2: return 2

        memo={}

        for m in range(n):
            memo[(n, m)]=0

        def dfs(s):
            if s in memo: return
            
            m, copied_m=s

            F=[float('inf')]
            
            if copied_m!=0:
                m_p=m+copied_m
                if m_p<=n:
                    copied_m_p=copied_m
                    s_p=m_p,copied_m_p
                    dfs(s_p)
                    F.append(memo[s_p]+1)

            if copied_m!=m:
                m_p=m
                copied_m_p=m
                s_p=m_p,copied_m_p
                dfs(s_p)
                F.append(memo[s_p]+1)

            memo[s]=min(F)
    
        dfs((1,0))
        return memo[(1,0)]