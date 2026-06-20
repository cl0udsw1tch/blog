class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # stage_n: current cut being made, producing the n, n+1 substring
        # state s_n: The substring after the (n-1)th cut (index of first elem)
        # decision x_n: where the nth cut is placed, (index of first elem of 
        #       right split) 
        #       => s_{n+1} is the right substring after cutting s_n at x_n
        # f_n(s_n, x_n): total num changes after cutting at x_n and making
        #       optimal cuts henceforth
        #       =>  = x_n + f*_{n+1}(s_{n+1})
        # f*_n(s_n) = min {f_n(s_n, x_n)} the optimal position x*_n to cut

        if len(s) == k:
            return 0
        if k == 1:
            numChanges = 0
            for i in range(math.floor(len(s)/ 2)):
                numChanges+=int(s[i]!=s[-1-i])
            return numChanges

        # at stage n, only need dp[n] and dp[n+1], so we wont store full table
        dp = [[], []] # stage_n, stage_{n+1}
        # stage k (no cuts left to make)
        stage_n = dp[0]  
        for s_n in range(k-1, len(s)): 
            #all possible substrings since previous k-1 substrings must have at least 1 element each => 0..k-2 are taken
            i=0
            f_star = 0
            ss_n = s[s_n:]
            for i in range(math.floor(len(ss_n)/ 2)):
                f_star+=int(ss_n[i]!=ss_n[-1-i])
            stage_n.append(f_star)
        dp[1] = dp[0]
        dp[0] = []

        # rest stages
        for n in range(k-1, 1, -1):
            stage_n = dp[0]
            stage_np1 = dp[1]
            # the nth substring must be made after the n-1 first substrings, 
            # before the last (k-n) substrings
            for s_n in range(n-1, len(s)-(k-n)):
                f = []
                for x_n in range(s_n+1, len(s)-(k-n-1)): 
                    #making the nth cut to create the next substring
                    ss_n = s[s_n:x_n]
                    ss_np1 = s[x_n:]
                    numChanges=0 
                    for i in range(math.floor(len(ss_n)/ 2)):
                        numChanges+=int(ss_n[i]!=ss_n[-1-i])
                    f.append(numChanges+stage_np1[x_n-n])
                f_star = min(f)
                stage_n.append(f_star)
            dp[1] = stage_n
            dp[0] = []
    
        # the first stage does not proceed a previous cut, so there is only one s_n = 0
        stage_n = dp[0]
        stage_np1 = dp[1]
        s_n=0
        f=[]
        for x_n in range(1, len(s) - (k-2)): 
            # need minimum k - 2 slots to fill the rest of the substrings after the first and second
            ss_n = s[s_n:x_n]
            ss_np1 = s[x_n:]
            numChanges=0
            for i in range(math.floor(len(ss_n)/ 2)):
                numChanges+=int(ss_n[i]!=ss_n[-1-i])
            f.append(numChanges+stage_np1[x_n-1])
        f_star = min(f)
        stage_n.append(f_star)
        return f_star
 
        