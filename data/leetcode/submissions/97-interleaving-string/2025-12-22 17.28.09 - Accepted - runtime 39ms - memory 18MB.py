class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3: return True
        if len(s3) != len(s1)+len(s2): return False
        if not s1: return s2==s3
        if not s2: return s1==s3

        '''
        s=last string used, index of last char added, largest index added from other string
        '''

        M,N,O=len(s1),len(s2),len(s3)
        memo={}
        memo[(M,N,O)]=True
        
        def dfs(s):
            if s in memo: return

            m, n, o=s
            F=False
            # add from s1
            if m<M and o<O and s3[o]==s1[m]:
                m_p,n_p,o_p=m+1,n,o+1
                s_p=(m_p, n_p, o_p)
                dfs(s_p)
                F=F or memo[s_p]
                if F:
                    memo[s]=True
                    return
            # add from s2
            if n<N and o<O and s3[o]==s2[n]:
                m_p,n_p,o_p=m,n+1,o+1
                s_p=(m_p, n_p, o_p)
                dfs(s_p)
                F=F or memo[s_p]
                if F:
                    memo[s]=True
                    return
            memo[s]=False

        dfs((0,0,0))
        return memo[(0,0,0)]


