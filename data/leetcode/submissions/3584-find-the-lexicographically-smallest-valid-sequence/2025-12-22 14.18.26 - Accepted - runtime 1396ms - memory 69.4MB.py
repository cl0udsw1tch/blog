class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        '''
        f*_m = longest suffix of word2 (identified by starting index) that is a subsequence of word1[m:]

        '''
        M,N=len(word1),len(word2)
        if N==1:
            return [0]

        dp=[[0] for _ in range(M)]
        dp[-1][0]=N-1 if (word2[-1] == word1[-1]) else N
        for m in range(M-2,-1,-1):
            stage_m=dp[m]
            stage_mp1=dp[m+1]
            stage_m[0]=max(0, stage_mp1[0]-1) if word2[stage_mp1[0]-1]==word1[m] else stage_mp1[0]

        r,ptr2,ptr1,remaining=[],0,0,1
        _n = lambda m: dp[m][0]

        while ptr2<N and ptr1<M and ptr2<_n(ptr1):
            if ptr1+1<M and ptr2==_n(ptr1)-1 and _n(ptr1+1)==_n(ptr1):
                r.append(ptr1)
                remaining=int(word1[ptr1]==word2[ptr2])
                ptr1,ptr2=ptr1+1,ptr2+1
                break    
            elif word1[ptr1]==word2[ptr2]:
                r.append(ptr1)
                ptr1,ptr2=ptr1+1,ptr2+1
            else:
                ptr1+=1

        while ptr1<M and ptr2 < N:
            if remaining:
                remaining-=int(word1[ptr1]!=word2[ptr2])
                r.append(ptr1)
                ptr1,ptr2=ptr1+1,ptr2+1 
            else:
                if word1[ptr1]!=word2[ptr2]:
                    ptr1+=1
                    continue 
                r.append(ptr1)
                ptr1,ptr2=ptr1+1,ptr2+1

        return r if len(r) == N else []







        
        