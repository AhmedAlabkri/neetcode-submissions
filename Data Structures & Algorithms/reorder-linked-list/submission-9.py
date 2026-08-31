# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # partitioning
        secondList = slow.next
        slow.next = None
        firstList = head

        # flipping second list

        curr = secondList
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        secondList = prev


        # constructing the list
        while secondList:
            tmp1, tmp2 = firstList.next, secondList.next
            firstList.next = secondList
            secondList.next = tmp1
            firstList, secondList = tmp1, tmp2

        




            
        