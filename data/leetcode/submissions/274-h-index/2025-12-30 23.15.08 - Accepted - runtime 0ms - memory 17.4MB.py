class Solution:
    def hIndex(self, citations: List[int]) -> int:
        M=len(citations)
        if M==1:
            return 1 if citations[0] else 0
        citations.sort(reverse=True)


        ptr=0
        while ptr<M and ptr < citations[ptr]:
            ptr+=1
        return ptr
        