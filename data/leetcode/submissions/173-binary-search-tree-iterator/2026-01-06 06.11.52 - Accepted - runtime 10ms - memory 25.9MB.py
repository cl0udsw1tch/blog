# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self._next=-float('inf')
        self.ancestor_stack=[]

    def next(self) -> int:

        if isinstance(self._next,float):
            node=self.root
            while node.left:
                self.ancestor_stack.append(node)
                node=node.left
            self._next=node
            return node.val
        else:
            if self._next.right: #go down right, go down left
                if not self._next.right.left:
                    self._next=self._next.right
                    return self._next.val

                node=self._next.right
                while node.left:
                    self.ancestor_stack.append(node)
                    node=node.left
                self._next=node
                return self._next.val
                
            else:
                self._next=self.ancestor_stack.pop()
                return self._next.val

          
    
    def hasNext(self) -> bool:
        
        if isinstance(self._next, float): return True
        return self._next.right is not None or len(self.ancestor_stack)>0




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()