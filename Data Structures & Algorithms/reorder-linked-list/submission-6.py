# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        firstList = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondList = slow.next
        slow.next = None
        
        curr = secondList
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        secondList = prev

        while secondList:
            tmp1, tmp2 = firstList.next, secondList.next
            firstList.next = secondList
            secondList.next = tmp1
            firstList, secondList = tmp1, tmp2

        



