# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1,ptr2=l1,l2

        rem=0
        total=ListNode(-1,None)
        prev=total
        m=0
        while ptr1 and ptr2:
            POW=10**m
            d1,d2=ptr1.val,ptr2.val

            prev.next=ListNode(val=(d1+d2+rem)%10, next=None)
            prev=prev.next
            rem=(d1+d2+rem)//10

            m+=1
            ptr1,ptr2=ptr1.next,ptr2.next

        while ptr1:
            POW=10**m
            d1=ptr1.val

            prev.next=ListNode(val=(d1+rem)%10, next=None)
            prev=prev.next
            rem=(d1+rem)//10

            ptr1=ptr1.next
            m+=1

        while ptr2:
            POW=10**m
            d2=ptr2.val

            prev.next=ListNode(val=(d2+rem)%10,next=None)
            prev=prev.next
            rem=(d2+rem)//10

            ptr2=ptr2.next
            m+=1

        if rem:
            prev.next=ListNode(val=1,next=None)
        return total.next