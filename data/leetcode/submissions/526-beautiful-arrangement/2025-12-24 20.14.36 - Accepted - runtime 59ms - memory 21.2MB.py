class Solution:
    def countArrangement(self, n: int) -> int:
        M=n
        if M==1:
            return 1
        
        memo={}
        memo[(M, 2**M-1)]=1

        def dfs(s):
            if s in memo: return

            m, mask = s
            m_p=m+1
            F=[]
            for x in range(M):
                if (1<<x) & mask: continue
                pos=x+1
                if pos%m_p and m_p%pos: continue
                mask_p=mask|(1<<x)
                s_p=m_p,mask_p
                dfs(s_p)
                F.append(memo[s_p])
            f_sum=sum(F)
            memo[s]=f_sum
        dfs((0,0))
        return memo[(0,0)]










