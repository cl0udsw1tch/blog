# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left==right: return head

        i=0
        start=ListNode(val=float('inf'))
        prev=start
        prev.next=head
        while i<left-1:
            prev=prev.next
            i+=1

        prev_left,_left=prev,prev.next

        node_i=None
        node_ip1=_left
        while i<right:
            tmp=node_ip1.next
            node_ip1.next=node_i

            node_i=node_ip1
            node_ip1=tmp
            i+=1

        _right=node_i
        right_next=node_ip1
        
        prev_left.next=_right
        _left.next=right_next

        
        return start.next
