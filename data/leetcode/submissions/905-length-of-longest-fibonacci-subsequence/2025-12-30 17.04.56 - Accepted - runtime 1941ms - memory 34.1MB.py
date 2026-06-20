class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        

        M=len(arr)
        if M<3: return 0

        index={v: i for i,v in enumerate(arr)}

        dp=[[0 for _ in range(M)] for _ in range(M)]
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            for s_m in range(m+1,M):
                next=index.get(arr[m]+arr[s_m], -1)
                if next==-1:
                    dp[m][s_m]=2
                    continue
                f=1 + dp[s_m][next]
                stage_m[s_m]=f
        r= max([l for stage in dp[:-2] for l in stage])
        return r if r>2 else 0