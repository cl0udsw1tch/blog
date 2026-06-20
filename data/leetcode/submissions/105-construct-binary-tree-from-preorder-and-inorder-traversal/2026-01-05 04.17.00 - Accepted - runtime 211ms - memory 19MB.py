# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        M=len(preorder)
        if M==1: return TreeNode(val=preorder[0])

        in_map={v:i for i,v in enumerate(inorder)}

        def dfs(i_pre,l_in,sz):
            if sz==0: 
                return None
            if sz==1:
                return TreeNode(val=preorder[i_pre])
                
            root=TreeNode(val=preorder[i_pre])

            root_in=in_map[root.val]

            left_sz=root_in-l_in
            right_sz=l_in+sz-1-root_in

            left_i_pre=i_pre+1
            right_i_pre=left_i_pre
            while right_i_pre<M and in_map[preorder[right_i_pre]]<root_in:
                right_i_pre+=1

            root.left,root.right=dfs(left_i_pre,l_in,left_sz),dfs(right_i_pre,root_in+1,right_sz)

            return root

        return dfs(0,0,M)
            
            

