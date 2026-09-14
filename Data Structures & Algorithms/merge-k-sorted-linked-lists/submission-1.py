# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergesort(a):
            if len(a) <= 1:
                return a[0]
            mid = len(a) // 2

            l = mergesort(a[:mid])
            r = mergesort(a[mid:])

            return merge(l, r)

        def merge(left, right):
            dummy = ListNode()
            tail = dummy

            while left and right:
                if left.val <= right.val:
                    tail.next = left
                    tail = tail.next
                    left = left.next
                else:
                    tail.next = right
                    tail = tail.next
                    right = right.next
            while left:
                tail.next = left
                tail = tail.next
                left = left.next
            while right:
                tail.next = right
                tail = tail.next
                right = right.next
            return dummy.next

        if not lists:
            return None
        return mergesort(lists)



