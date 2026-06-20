class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        '''
        f*_m(s_m): over nums[m:]: max value, position of ( after
        s: max/min
        x: place/not place (

        '''
        M=len(nums)
        if M==1: return str(nums[0])
        if M==2: return str(nums[0]) + "/" + str(nums[1])

        dp=[[(0,0), (0,0)] for _ in range(M+1)]
        dp[-1]=[(1, ()), (1, ())]
        dp[-2]=[(nums[-1], ()), (nums[-1], ())]

        for m in range(M-2,-1,-1):
            for s_m in range(2):
                F=[]
                s_mp1=int(not s_m)

                for x_m in range(m, M):
                    f_mp=dp[x_m+1][s_mp1]
                    f=nums[m]
                    for i in range(m+1, x_m+1):
                        f/=nums[i]
                    f=f/f_mp[0], (((x_m,) + f_mp[1]) if x_m<M-2 else ())
                    F.append(f)
                
                f_ext=(max if s_m else min)(F, key=lambda f: f[0])
                dp[m][s_m]=f_ext

        best_placements=dp[0][1][1]
        num_parentheses = len(best_placements)
        if num_parentheses == 0:
            return "/".join(list(map(str, nums)))
        r=""
        n=0
        for m in range(M):
            r+=str(nums[m])+"/"
            if n<num_parentheses and best_placements[n]==m:
                r+="("
                n+=1
        r=r[:-1] + ")"*num_parentheses
        return r
        
            