# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        slow, fast = dummy, head
        #reach nth node from start
        while n:
            fast = fast.next
            n-=1
        
        #reach nth-1 node with slow
        while fast:
            fast=fast.next
            slow=slow.next
        
        slow.next=slow.next.next

        return dummy.next
