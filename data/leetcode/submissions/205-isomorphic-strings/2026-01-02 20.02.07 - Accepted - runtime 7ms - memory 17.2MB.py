class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        M,N=len(s),len(t)
        if M==1 and N==1: return True
        
        s_dict,t_dict={},{}
        for m in range(M):
            c,d=s[m],t[m]
            if c in s_dict:
                if s_dict[c]!=d: return False
            elif d in t_dict:
                return False
            else:
                s_dict[c]=d
                t_dict[d]=c
        return True