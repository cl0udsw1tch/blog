"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        if not head.next:
            node=Node(x=head.val, next=None)
            node.random=node if head.random else None
            return node

        start=Node(x=0)
        prev=start
        node=head
        while node:
            node_copy=Node(x=node.val)
            node_next=node.next

            prev.next=node
            node.next=node_copy

            prev=node_copy
            node=node_next
        
        old=start.next
        while old:
            old_random=old.random
            new=old.next
            if old_random:
                new.random=old_random.next
            old=new.next

        prev=start
        node=start.next
        while node:
            prev.next=node.next
            prev=node.next
            node=node.next.next

        return start.next


