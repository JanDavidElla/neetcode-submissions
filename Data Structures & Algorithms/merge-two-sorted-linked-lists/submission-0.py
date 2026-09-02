# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        use two pointers, one for list1, another for list 2, 
        1. compare
        - smallest one gets picked and curr of that list updates
        """
        merge = ListNode(None, None)   
        head = merge

        i = list1
        j = list2

        while i != None and j != None:

            if i.val <= j.val:
                merge.next = ListNode(i.val)
                i = i.next
            else:
                merge.next = ListNode(j.val)
                j = j.next
            merge = merge.next
        
        if i != None:
            merge.next = i
        elif j != None:
            merge.next = j
        
        return head.next