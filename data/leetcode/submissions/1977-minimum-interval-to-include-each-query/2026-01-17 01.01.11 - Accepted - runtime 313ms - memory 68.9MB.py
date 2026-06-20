class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        N=len(queries)
        intervals.sort(key=lambda i: i[0])
        q=deque(intervals)
        query_idxs={v:i for i,v in enumerate(sorted(list(range(N)), key=lambda idx: queries[idx]))}
        queries.sort()
        heap=[]
        ans=[]
        for query in queries:
            while q and q[0][0]<=query:
                _int=q.popleft()
                _len,l,r=_int[1]-_int[0]+1, _int[0], _int[1]
                heapq.heappush(heap,(_len,l,r))
            while heap and heap[0][2]<query:
                heapq.heappop(heap)
            ans.append(heap[0][0] if heap else -1)
            
        return [ans[query_idxs[i]] for i in range(N)]



