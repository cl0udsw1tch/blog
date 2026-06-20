class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        hBars.sort()
        vBars.sort()
        def max_subarray_dp(arr):
            M=len(arr)
            dp=[0] * M
            dp[M-1]=1
            for m in range(M-2,-1,-1):
                dp[m]=(dp[m+1]+1) if arr[m]==arr[m+1]-1 else 1
            return max(dp)

        max_h_del=max_subarray_dp(hBars)
        max_v_del=max_subarray_dp(vBars)
        #print(max_h_del,max_v_del)
        return (min(max_h_del,max_v_del)+1)**2
