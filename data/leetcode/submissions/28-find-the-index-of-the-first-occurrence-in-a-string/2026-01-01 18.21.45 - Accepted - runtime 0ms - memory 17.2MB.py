class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        M=len(haystack)
        N=len(needle)
        if N>M:return -1
        if N==M: return -1 if haystack!=needle else 0

        ptr1,ptr2=0,0
        while ptr1<M and ptr2<N and ptr1+ptr2<M :
            if haystack[ptr1+ptr2]!=needle[ptr2]:
                ptr1+=1
                ptr2=0
            elif haystack[ptr1+ptr2]==needle[ptr2]:
                ptr2+=1
                if ptr2==N: return ptr1
        return -1