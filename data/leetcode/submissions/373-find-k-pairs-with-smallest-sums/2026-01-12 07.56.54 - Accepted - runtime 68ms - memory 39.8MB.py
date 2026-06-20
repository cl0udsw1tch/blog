class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        M,N=len(nums1),len(nums2)

        r=[]
        heap=[(nums1[0]+nums2[0], 0, 0)]
        seen={}
        seen[(0,0)]=True
        while len(r)<k:
            _,i,j=heapq.heappop(heap)
            r.append([nums1[i],nums2[j]])
            
            if i+1<M and (i+1,j) not in seen:
                heapq.heappush(heap, (nums1[i+1]+nums2[j],i+1,j))
                seen[(i+1, j)]=True
            if j+1<N and (i,j+1) not in seen:
                heapq.heappush(heap, (nums1[i]+nums2[j+1],i,j+1))
                seen[(i,j+1)]=True
        return r