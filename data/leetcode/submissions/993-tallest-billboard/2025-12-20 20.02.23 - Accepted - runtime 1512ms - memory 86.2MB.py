class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        '''
        f*(s) gives future sum 
        state: s=(diff = A-B)

        '''
        M=len(rods)
        if M==1: return 0
        if M==2: return int(rods[1]==rods[0])*rods[1]

        memo={}
        def dfs(s):
            if s in memo: return
            m,remainingA=s
            if m==M-1:
                if abs(remainingA)==rods[M-1]:
                    memo[s]=rods[M-1] 
                elif remainingA==0:
                    memo[s]=0
                else:
                    memo[s]= -float('inf')
                return
            rod_m=rods[m]
            F=[0]*3
            for i,x_m in enumerate(["skip", "A", "B"]):
                if x_m=='skip':
                    s_p=(m+1, remainingA)
                    dfs(s_p)
                    F[i]=memo[s_p]
                elif x_m=="A":
                    s_p=(m+1, remainingA-rod_m)
                    dfs(s_p)
                    F[i]=memo[s_p]+rod_m
                else:
                    s_p=(m+1, remainingA+rod_m)
                    dfs(s_p)
                    F[i]=memo[s_p]+rod_m
            f_min=max(F)
            memo[s]=f_min
        
        dfs((0,0))
        return memo[(0,0)] // 2 if not math.isinf(memo[(0,0)]) else 0


