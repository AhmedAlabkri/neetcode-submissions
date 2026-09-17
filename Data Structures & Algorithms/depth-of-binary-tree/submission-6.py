# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lvl = 1
        stack = [(root, 1)]
        while stack:
            r, _ = stack.pop()
            if r:
                lvl = max(lvl, _)
                stack.append((r.left, _+1))
                stack.append((r.right, _+1))
        return lvl
            


        
        
        