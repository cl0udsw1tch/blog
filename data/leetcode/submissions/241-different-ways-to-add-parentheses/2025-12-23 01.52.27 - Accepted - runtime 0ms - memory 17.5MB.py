class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        M=len(expression)
        if M==1:
            return [int(expression[0])]

        memo={}

        Nums=()
        Ops=()
        i=0
        while i < M:
            curr_num=""
            while i<M and expression[i] not in  ["-","+","*"]:
                curr_num+=expression[i]
                i+=1
            if curr_num:
                Nums+=(int(curr_num),)
            else:
                Ops+=(expression[i],)
                i+=1


        def dfs(s):
            if s in memo:
                return
            nums, ops=s
            assert(len(ops)==len(nums)-1)

            if len(ops)==0:
                memo[s] = [nums[0]]
                return

            if len(ops)==1:
                memo[s]=[nums[0] + nums[1] if ops[0]=="+" else (nums[0]-nums[1] if ops[0]=="-" else nums[0] * nums[1])]
                return

            F=[]
            for x in range(0, len(ops)):
                l_nums, op, r_nums= nums[:x+1], ops[x], nums[x+1:]
                l_ops, r_ops = ops[:x], ops[x+1:]

                dfs((l_nums, l_ops))
                dfs((r_nums, r_ops))

                for u in memo[(l_nums, l_ops)]:
                    for v in memo[(r_nums, r_ops)]:
                        F.append(u + v if op=="+" else (u - v if op=="-" else u*v))

            memo[s]=F

        dfs((Nums, Ops))
        return memo[(Nums, Ops)]