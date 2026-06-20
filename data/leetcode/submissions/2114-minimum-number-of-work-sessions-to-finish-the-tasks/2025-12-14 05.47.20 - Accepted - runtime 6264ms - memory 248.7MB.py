class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        '''
        f*(s:mask,lap_time) = min num sessions that must **terminate** to finish remaining tasks, 
        assuming tasks in mask have been done and  lap_time minutes has elapsed from current session
        s: (mask, lap_time)
        '''
        M=len(tasks)
        if M==1: return 1

        memo={} 
        for lap_time in range(sessionTime):
            memo[(2**M-1, lap_time)]=0 if not lap_time else 1

        def dfs(s):
            if s in memo: return
            mask, lap_time = s
            F=[]
            for x in range(M):
                if (1<<x) & mask: continue
                mask_p = mask | (1<<x)
                lap_time_p = ((lap_time + tasks[x]) % sessionTime) if lap_time + tasks[x] <= sessionTime else tasks[x]%sessionTime
                s_p=(mask_p, lap_time_p)
                dfs(s_p)
                f=memo[s_p] + int(lap_time + tasks[x] >= sessionTime) + int(tasks[x]==sessionTime and lap_time>0)
                F.append(f)
            f_min=min(F)
            memo[s]=f_min

        dfs((0,0))
        return memo[(0,0)]