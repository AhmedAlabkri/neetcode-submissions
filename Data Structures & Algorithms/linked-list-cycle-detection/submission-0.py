# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        hMap = set()
        while curr:
            if curr not in hMap:
                hMap.add(curr)
                curr = curr.next
            else:
                return True
        
        return False
            


            