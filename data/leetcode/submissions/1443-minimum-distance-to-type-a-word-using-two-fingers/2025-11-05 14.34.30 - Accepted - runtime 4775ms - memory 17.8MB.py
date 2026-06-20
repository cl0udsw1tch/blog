class Solution:
    def minimumDistance(self, word: str) -> int:
        '''
        stage_n: the index of the letter being typed 
        s_n: letter both fingers are on (c1, c2)
        x_n: possible destinations to c3, 2 options
            => (c1, c3) OR (c3, c2)
            => s_{n+1} = x_n
        f_n(s_n, x_n) = |x_n-s_n| + f*_{n+1}(s_{n+1})
        f*_n(s_n) = min_{x_n} f_n(s_n, x_n)

        '''
        width=6
        height=5
        N=len(word)

        if N < 3:
            return 0

        char2Pos = lambda c : ((ord(c)-ord('A')) // width, (ord(c)-ord("A"))%width)
        def chars2Dist(c, d):
            c_pos=char2Pos(c)
            d_pos=char2Pos(d)
            return abs(c_pos[0]-d_pos[0]) + abs(c_pos[1]-d_pos[1])

        letters=""
        for c in word:
            letters+=(c if c not in letters else "")
        M=len(letters)
        
        dp=[[],[]]
        for i,c1 in enumerate(letters):
            for j,c2 in enumerate(letters):
                dp[1].append(((c1, c2), 0))

        for n in range(N-2, -1, -1):
            stage_n=dp[0]
            stage_np1=dp[1]
            c3=word[n+1]
            k=letters.find(c3)

            for i,c1 in enumerate(letters):
                for j,c2 in enumerate(letters):
                    if c2==c1: 
                        stage_n.append(((c1, c2), math.inf))
                        continue
                    s_n=(c1, c2)
                    f_star=0
                    F=[]
                    x_n=(c1,c3)
                    f=chars2Dist(c2,c3)+stage_np1[i*M+k][1]
                    F.append((s_n,f))
                    x_n=(c3,c2)
                    f=chars2Dist(c1,c3)+stage_np1[k*M+j][1]
                    F.append((s_n,f))

                    f_star =min(F, key=lambda x: x[1])
                    stage_n.append(f_star)
            dp[1]=stage_n
            dp[0]=[]
            
        r = min([d for d in dp[1] if word[0] in d[0]], key=lambda x: x[1])[1]

        return(r)



            

        




