class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        M=len(profits)
        total=w
        heap1=[(capital[i],profits[i]) for i in range(M)]
        heapq.heapify(heap1)

        heap2=[]

        for _ in range(k):
            while heap1 and heap1[0][0]<=total:
                cap,prof=heapq.heappop(heap1)
                heapq.heappush_max(heap2,prof)
            if not heap2: return total
            total+=heapq.heappop_max(heap2)

        return total