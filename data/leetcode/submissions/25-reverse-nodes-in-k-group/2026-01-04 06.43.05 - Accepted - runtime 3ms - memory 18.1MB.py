# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        start=ListNode(val=float('inf'))
        start.next=head

        left_prev,left=start,head
        prev=start
        i=0
        while True:
            while i<k:
                if not prev.next:
                    return start.next
                prev=prev.next
                i+=1
                
            right=prev
            right_next=prev.next

            node_i=None
            node_ip1=left
            i=0
            while i<k:
                node_next=node_ip1.next
                node_ip1.next=node_i
                node_i=node_ip1
                node_ip1=node_next
                i+=1
            left_prev.next=right
            left.next=right_next

            i=0
            prev=left
            left_prev=left
            left=right_next
            
