class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        M=len(gas)
        if M==1:
            return 0 if cost[0]<=gas[0] else -1
        
        if sum(cost)>sum(gas): return -1

        MIN=0,float('inf')
        curr=0
        for i in range(M):
            curr=curr+gas[i]-cost[i]
            if curr<MIN[1]:
                MIN=((i+1)%M),curr

        return MIN[0]

        

