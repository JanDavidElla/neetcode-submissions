# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Keep track of indices

i 

0, n-i, (i+1), n - (i+1), and so on

i = counter, starts at 0

n = len(listNode)

curr = 0, i+1, etc.

end = len(listNode) - 1



"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeList = []
        curr = head
        while curr:
            nodeList.append(curr.val)
            curr = curr.next
    
        #two pointer approach

        i = 1
        j = len(nodeList) - 1
        print(nodeList)

        while i <= j:
            head.next = ListNode(nodeList[j])

            if j == i:
                break

            head.next.next = ListNode(nodeList[i])
            i = i + 1
            j = j - 1
            head = head.next.next

        