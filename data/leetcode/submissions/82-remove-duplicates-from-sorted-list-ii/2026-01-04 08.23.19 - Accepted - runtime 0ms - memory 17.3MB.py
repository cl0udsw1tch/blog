# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=ListNode(val=float('inf'))
        start.next=head

        prev=start
        node=head

        while node:
            val=node.val
            skip=node.next and node.next.val==val
            while node.next and node.next.val==val:
                node=node.next
            if skip:
                prev.next=node.next
            else:
                prev=node
            node=node.next
        return start.next