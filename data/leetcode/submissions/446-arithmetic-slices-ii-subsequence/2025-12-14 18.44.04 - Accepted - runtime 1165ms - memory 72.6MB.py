class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        f*((s1,s2)): number of arithmetic sequences in nums[s1:] with interval s2
        x: choose or skip nums[s]
        '''

        M=len(nums)
        print(M)
        if M<3: return 0
        if M==3: return int(nums[1]-nums[0] == nums[2]-nums[1])

        diff = lambda m, n: nums[max(m,n)]-nums[min(m,n)]
        
        dp=[defaultdict(int) for _ in range(M)]
        dp[M-2][diff(M-2, M-1)]=1

        self.total=0

        for m in range(M-3,-1,-1):
            stage_m=dp[m]

            states=defaultdict(list) 
            for n in range(m+1,M):
                states[diff(m,n)].append(n)

            for s_m in states:
                f_sum=0
                for x_m in states[s_m]:
                    s_mp1=s_m
                    mp1=x_m
                    f_mp1=dp[mp1][s_mp1]
                    self.total+=f_mp1
                    f_sum+=f_mp1+1
                stage_m[s_m]=f_sum

        return self.total