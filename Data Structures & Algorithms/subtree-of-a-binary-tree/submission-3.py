# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.candidate = subRoot.val
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left == -1 or right == -1:
                return -1

            if curr.val == self.candidate:
                if potentialSubTree(curr, subRoot):
                    return -1
            """if curr.left and curr.left.val == self.candidate:
                if potentialSubTree(curr.left, subRoot):
                    return -1
            if curr.right and curr.right.val == self.candidate:
                if potentialSubTree(curr.right, subRoot):
                    return -1"""

            return max(left,right) + 1

        def potentialSubTree(curr, subRoot):
            if not (curr or subRoot):
                return True
            if not (curr and subRoot):
                return False
            if curr.val != subRoot.val:
                return False
            left = potentialSubTree(curr.left, subRoot.left)
            right = potentialSubTree(curr.right, subRoot.right)
            return left and right


        if dfs(root) != -1:
            return False
        return True