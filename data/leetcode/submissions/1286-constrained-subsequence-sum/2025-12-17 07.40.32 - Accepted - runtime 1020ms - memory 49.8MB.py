class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        '''
        
        '''
        M=len(nums)
        if M==1: return nums[0]
        
        dp=[[-float('inf')] for _ in range(M)]
        dp[-1]=[nums[-1]]

        heap=[(-nums[-1], M-1)]
        heapq.heapify(heap)
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            #take
            s_m=0
            while heap[0][1] > m+k: heapq.heappop(heap)
            f_max=nums[m] + max(0, -heap[0][0])
            stage_m[s_m]=f_max
            heapq.heappush(heap, (-stage_m[s_m], m))

        return max(dp, key = lambda stage: stage[0])[0]
