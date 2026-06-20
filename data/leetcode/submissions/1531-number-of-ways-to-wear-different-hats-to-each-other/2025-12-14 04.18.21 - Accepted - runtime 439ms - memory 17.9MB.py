class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        '''
        f*(m, h): gives #ways to satisfy remaining people given: mask m have been satisfied using hats < h
        s: (m, h) where m = 0...2**M-1, h=1...40
        x: skip hat h+1 or assign it to any person 
        '''
        M=40
        N=len(hats)
        if N==1:
            return len(hats[0])

        preferences = [hat for person in hats for hat in person]
        minHat, maxHat =min(preferences), max(preferences)
        
        dp=[[], [0 for _ in range(1<<N)]]
        # m=maxHat+1
        stage_m=dp[1]
        stage_m[2**N-1]=1

        for m in range(maxHat, minHat-1,-1):
            stage_m=[0 for _ in range(1<<N)]
            stage_mp1=dp[1]

            for s_m in range(1<<N):
                F=[]

                # skip hat m
                s_mp1=s_m
                f=stage_mp1[s_mp1]
                F.append(f)

                #use hat m
                for i,person in enumerate(hats):
                    if m in person and not ((1<<i) & s_m):
                        s_mp1 = s_m | (1<<i)
                        f=stage_mp1[s_mp1]
                        F.append(f)
                f_sum=sum(F)
                stage_m[s_m]=f_sum
            dp[1]=stage_m

        return dp[1][0] % (10**9 + 7)
        
