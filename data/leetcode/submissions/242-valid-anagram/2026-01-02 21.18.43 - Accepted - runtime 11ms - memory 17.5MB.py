class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        M,N=len(s),len(t)
        if M!=N: return False

        s_dict=defaultdict(int)
        for c in s:
            s_dict[c]+=1
        for c in t:
            if s_dict[c]==0:
                return False
            s_dict[c]-=1
        return True