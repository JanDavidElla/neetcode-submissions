# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        current = head
        if current.next == None:
            return current
        
        right = current.next
        left = current
        current.next = None
        current = right

        while current.next:
            
            right = current.next
            current.next = left # does the reversal

            left = current
            current = right
        current.next = left

        return current
