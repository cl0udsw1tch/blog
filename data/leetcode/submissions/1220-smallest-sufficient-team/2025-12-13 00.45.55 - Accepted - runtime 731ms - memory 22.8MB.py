class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        M=len(req_skills)
        N=len(people)
        if M==1:
            return 0
        skills_map={skill: i for (i, skill) in enumerate(req_skills)}

        memo={}
        memo[2**M-1]=0

        def dfs(s):
            if s in memo: return
            F=[2**N-1]*N
            for x_m in range(N):
                s_p=s
                for skill in people[x_m]:
                    i=skills_map[skill]
                    s_p=s_p | (1<<i)
                if s==s_p: continue
                dfs(s_p)
                f=memo[s_p] | (1<<x_m)
                F[x_m]=f
            f_min=min(F, key=lambda x: x.bit_count())
            memo[s]=f_min
        
        dfs(0)
        return [j for j in range(N) if (1<<j)&memo[0]]