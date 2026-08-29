# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        secondList = prev
        firstList = head


        while secondList:
            tmp1, tmp2 = firstList.next, secondList.next
            firstList.next = secondList
            secondList.next = tmp1
            firstList, secondList = tmp1, tmp2
        
        if firstList:
            firstList = firstList.next
            



        




        



        


        