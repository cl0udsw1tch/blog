class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        M=len(strs)
        if M==1:
            return [strs]
        ss=[s for s in strs]
        for m in range(M): ss[m]="".join(sorted(ss[m]))
        ss=sorted(list(enumerate(ss)), key = lambda s: s[1])
        
        r=[]
        s=[ss[0][0]]
        for m in range(1,M):
            if not s or ss[m][1]==ss[m-1][1]:
                s.append(ss[m][0])
            else:
                r.append(s)
                s=[ss[m][0]]
        if s: r.append(s)
        return [[strs[i] for i in g] for g in r]



