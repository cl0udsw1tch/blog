# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        '''
        stage_m: m=1...n subproblem f*_m(s_m) solves the problem for [m...s_m]
        x_m: which in [m...s_m] is the root
        f_m(s_m, x_m) = [left=f*_m(x_m-1), val=x_m, right=f*_{x_m+1}(s_m)]
        '''

        if n==1:
            return [TreeNode(val=1)]
        if n==2:
            return [TreeNode(val=1, right=TreeNode(val=2)), TreeNode(val=2, left=TreeNode(val=1))]

        inc = lambda x : x+1

        dp = [[[] for _ in range(n)] for _ in range(n)]
        dp[-1][-1]=[TreeNode(val=n)]
        dp[-2][-1]=[TreeNode(val=n-1, right=TreeNode(val=n)), TreeNode(val=n, left=TreeNode(val=n-1))]
        dp[-2][-2]=[TreeNode(val=n-1)]

        for m in range(n-3,-1,-1):
            for s_m in range(m, n):
                
                if s_m==m:
                    dp[m][s_m]=[TreeNode(val=inc(m))]
                    continue
                elif s_m==m+1:
                    dp[m][s_m]=[TreeNode(val=inc(m), right=TreeNode(val=inc(m)+1)), TreeNode(val=inc(m)+1, left=TreeNode(val=inc(m)))]
                    continue
                else:
                    F=[]
                    f=[None for _ in range(len(dp[m+1][s_m]))]
                    for i,tree in enumerate(dp[m+1][s_m]):
                        newTree=TreeNode(val=inc(m), right=tree)
                        f[i]=newTree
                    F.extend(f)
                    for x_m in range(m+1, s_m):
                        f=[None for _ in range(len(dp[m][x_m-1])*len(dp[x_m+1][s_m]))]
                        for i,tree1 in enumerate(dp[m][x_m-1]):
                            for j,tree2 in enumerate(dp[x_m+1][s_m]):
                                newTree=TreeNode(left=tree1, val=inc(x_m), right=tree2)
                                f[i*len(dp[x_m+1][s_m])+j]=newTree
                        F.extend(f)

                    f=[None for _ in range(len(dp[m][s_m-1]))]
                    for i,tree in enumerate(dp[m][s_m-1]):
                        newTree=TreeNode(left=tree, val=inc(s_m))
                        f[i]=newTree
                    F.extend(f)
 
                    dp[m][s_m]=F
                    
        return dp[0][-1]