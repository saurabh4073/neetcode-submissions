# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        #find mid
        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next
        
        #reverse second half
        prev , curr = None , slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next =prev
            prev= curr
            curr= nxt
        
        #merge the list
        second, first = prev, head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
