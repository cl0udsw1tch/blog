# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head

        start=ListNode(val=float('inf'))
        start.next=head
        prev=start
        while prev.next and prev.next.val<x:
            prev=prev.next
        if not prev.next: return head

        smaller=prev

        prev=smaller.next
        node=smaller.next.next

        while node:
            if node.val<x:
                larger=smaller.next
                node_next=node.next

                smaller.next=node
                node.next=larger
                smaller=node

                prev.next=node_next
                node=node_next
            else:
                prev=node
                node=node.next

        return start.next