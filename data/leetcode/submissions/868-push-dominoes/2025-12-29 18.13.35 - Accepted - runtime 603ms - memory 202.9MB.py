class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        M=len(dominoes)
        if M==1: return dominoes
        
        memo1={}
        memo1[0]=0
        for m in range(M):
            if dominoes[m]=="R":
                memo1[m]=1
            elif dominoes[m]=="L":
                memo1[m]=0
        memo1[M]=0

        def dfs1(s):
            if s in memo1: return

            dfs1(s-1)
            if memo1[s-1]==0:
                memo1[s]=0
            else:
                memo1[s]=memo1[s-1]+1
        
        for m in range(M):
            dfs1(m)
        
        memo2={}
        memo2[M]=0
        for m in range(M):
            if dominoes[m]=="L":
                memo2[m]=1
            elif dominoes[m]=="R":
                memo2[m]=0
        
        def dfs2(s):
            if s in memo2: return

            dfs2(s+1)
            if memo2[s+1]==0:
                memo2[s]=0
            else:
                memo2[s]=memo2[s+1]+1
        
        for m in range(M):
            dfs2(m)


        r=""
        for m in range(M):
            if dominoes[m]!=".":
                r+=dominoes[m]
            else:
                if memo1[m]==memo2[m]:
                    r+="."
                elif (memo1[m]<memo2[m] and memo1[m]!=0) or memo2[m]==0:
                    r+="R"
                else: r+="L"
        return r
        




