# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        M=len(inorder)
        if M==0: return None
        if M==1: return TreeNode(val=inorder[0])

        in_map={v:i for i,v in enumerate(inorder)}

        def dfs(post_idx, left_in, sz):
            if sz==0: return None
            if sz==1: return TreeNode(val=postorder[post_idx])

            node_in=in_map[postorder[post_idx]]
            l_left_in,r_left_in=left_in,node_in+1

            r_post_idx=post_idx-1
            l_post_idx=r_post_idx
            while in_map[postorder[l_post_idx]] > node_in:
                l_post_idx-=1
            
            l_sz,r_sz=node_in-l_left_in,l_left_in+sz-1-node_in

            root=TreeNode(val=postorder[post_idx])
            root.left,root.right=dfs(l_post_idx,l_left_in,l_sz),dfs(r_post_idx,r_left_in,r_sz)
            return root

        return dfs(M-1,0,M)


            