class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        stage_m: m=0...M-1 subproblem f*_m(s_m) solves the problem for str1[m:], str2[s_m:]
        s_m: index in str2
        x_m: deletion of str1[m]                   {str1[m+1:],str2[s_m:]}, => C_m = 1
             deletion of str2[s_m]                 {str1[m:],str2[s_m+1:]}, => C_m = 1
             doing nothing                          {str1[m+1:],str2[s_m+1:]} => C_m = 0
     
        f_m(s_m, x_m) = C_m + f*_m'(s_{m+1})
        f*_m(s_m) = min_{x_m}(f_m(s_m, x_m))

        '''

        M,N=len(str1),len(str2)
        if M==1:
            if str1[0] not in str2: return str1+str2
            return str2
        if N==1:
            if str2[0] not in str1: return str1 + str2
            return str1

        dp=[[0 for _ in range(N+1)] for _ in range(M+1)]

        X=[(1,0), (0,1), (1,1)]

        for m in range(M-1,-1,-1):
    
            stage_m=dp[m]

            for s_m in range(N-1,-1,-1):
                F=-float('inf')
                for x_m in X[:2]:
                    s_mp1=s_m+x_m[1]
                    mp=m+x_m[0]
                    f=dp[mp][s_mp1] if s_mp1<N else 0
                    F=max(F,f)
                if str1[m] == str2[s_m]:
                    s_mp1=s_m+1
                    mp=m+1
                    f=1+(dp[mp][s_mp1] if s_mp1<N else 0)
                    F=max(F,f)
                stage_m[s_m]=F


        r=""
        i,j=0,0
        while i < M and j < N:
            if str1[i]==str2[j]:
                r+=str1[i]
                i+=1
                j+=1
            elif dp[i+1][j] > dp[i][j+1]:
                r+=str1[i]
                i+=1
            else:
                r+=str2[j]
                j+=1


        r+=(str1[i:] if i < M else "") +(str2[j:] if j < N else "")
        
        #print(r)
        return r

            
         

