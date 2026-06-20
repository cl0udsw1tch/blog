class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        stage_k: k=0...K-1 subproblem f*_k(p,q) solves the problem for strs[k:K] given at most p 0s and q 1s allowed
        s_k: (s_k0, s_k1) = { 0 ... m } x { 0 ... n } = # of 0s and 1s to be covered by strs[k:K]
        x_k: keeping or skipping string ss_k with a 0s and b 1s
            => keeping: x_k = -(a, b) => s_{k+1} = s_k - (a,b)
            => skipping: x_k = (0,0) => s_{k+1} = s_k
            => s_{k+1} = s_k + x_k
        f_k(s_k, x_k) = int(x_k != (0,0)) + f*_{k+1}(s_{k+1})
        f*_k(s_k) = max_{x_k}{f_k(s_k, x_k)}

        '''

        K=len(strs)
        if K==1:
            return int(strs[0].count('0') <= m and strs[0].count('1') <= n)
        
        dp=[[],[[0 for _ in range(n+1)] for _ in range(m+1)]]
        str_n = strs[-1]
        a=str_n.count('0')
        b=str_n.count('1')
        if a<=m and b<=n:
            dp[-1][a][b]=1

        for k in range(K-2,-1,-1):
            stage_k=[[0 for _ in range(n+1)] for _ in range(m+1)]
            stage_kp1=dp[1]

            str_k=strs[k]
            a,b=str_k.count('0'),str_k.count('1')

            for i in range(0,m+1):
                for j in range(0,n+1):
                    s_k=(i,j)
                    F=[0,0]
                    x_n=(0,0)
                    s_kp1=s_k
                    f=stage_kp1[s_kp1[0]][s_kp1[1]]
                    F[0]=f
                    x_n=(-a,-b)
                    if i >= a and j >= b:
                        s_kp1=(i-a, j-b)
                        f=1+stage_kp1[s_kp1[0]][s_kp1[1]]
                        F[1]=f
                    f_max=max(F)
                    stage_k[s_k[0]][s_k[1]]=f_max
            
            dp[1]=stage_k
        
        return max(sum(dp[1], []))

