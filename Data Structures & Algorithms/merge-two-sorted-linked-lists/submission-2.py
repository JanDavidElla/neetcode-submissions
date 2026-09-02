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
        merge = ListNode()   
        head = merge

        while list1 and list2:

            if list1.val <= list2.val:
                merge.next = list1
                list1 = list1.next
            else:
                merge.next = list2
                list2 = list2.next
            merge = merge.next

        merge.next = list1 or list2
        
        return head.next