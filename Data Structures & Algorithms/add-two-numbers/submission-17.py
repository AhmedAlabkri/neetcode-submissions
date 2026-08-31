# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        r = dummy
        carry = 0

        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            # 11
            result = v1 + v2 + carry
            if result > 9:
                # 11 -> val 1 and carry 1
                carry = result // 10
                actualResult = result % 10
                r.next = ListNode(actualResult)
            else:
                r.next = ListNode(result)
                carry = 0
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            r = r.next
        
        if carry != 0:
            r.next = ListNode(carry)

        return dummy.next
            





