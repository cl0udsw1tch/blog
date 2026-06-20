class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        M=len(s)
        if M<=1:
            return M
        seen=defaultdict(bool)
        ptr1,ptr2=0,0
        r=0
        while ptr1<M and ptr2<M:
            c=s[ptr2]
            if not seen[c]:
                seen[c]=True
                ptr2+=1
                r=max(r, ptr2-ptr1)
                if ptr2==M: return r
            elif seen[c]:
                del seen[s[ptr1]]
                ptr1+=1
        return r



        